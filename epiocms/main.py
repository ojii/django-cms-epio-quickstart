from __future__ import with_statement
import os
import shutil
import subprocess
import sys

EPIO_APP_NOT_FOUND = 1
SUBPROCESS_FAILED = 2

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

def _run_command(bits):
    process = subprocess.Popen(bits, stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, shell=False)
    stdout, stderr = process.communicate()
    return (process.returncode, stdout, stderr)

def main():
    cwd = os.getcwd()
    epio_appfile = os.path.join(cwd, '.epio-app')
    with open(epio_appfile, 'r') as fobj:
        appname = fobj.read()
    print "Checking environment"
    if not os.path.exists(epio_appfile):
        print "Please run `epio create` first and run this command from within"
        print "the epio app directory."
        print >> sys.stderr, "File .epio-app not found"
        sys.exit(EPIO_APP_NOT_FOUND)
    print "Copying data"
    shutil.copytree(os.path.join(DATA_DIR, 'media'), os.path.join(cwd, 'media'))
    shutil.copytree(os.path.join(DATA_DIR, 'templates'), os.path.join(cwd, 'templates'))
    shutil.copy(os.path.join(DATA_DIR, 'epio.ini'), cwd)
    shutil.copy(os.path.join(DATA_DIR, 'requirements.txt'), cwd)
    shutil.copy(os.path.join(DATA_DIR, 'settings.py'), cwd)
    shutil.copy(os.path.join(DATA_DIR, 'urls.py'), cwd)
    print "Uploading app"
    print "This will take a couple of minutes, go grab a coffee!"
    retcode, stdout, stderr = _run_command(["epio", "upload"])
    if retcode != 0:
        print "Subprocess (epio upload) failed with status code %s" % retcode
        print >> sys.stderr, stdout
        print >> sys.stderr, stderr
        sys.exit(SUBPROCESS_FAILED)
    print "Syncing database"
    retcode, stdout, stderr = _run_command(["epio", "django", "--", "syncdb", "--all"])
    if retcode != 0:
        print "Subprocess (epio django -- syncdb --all) failed with status code %s" % retcode
        print >> sys.stderr, stdout
        print >> sys.stderr, stderr
        sys.exit(SUBPROCESS_FAILED)
    retcode, stdout, stderr = _run_command(["epio", "django", "--", "migrate", "--fake"])
    if retcode != 0:
        print "Subprocess (epio django -- migrate --fake) failed with status code %s" % retcode
        print >> sys.stderr, stdout
        print >> sys.stderr, stderr
        sys.exit(SUBPROCESS_FAILED)
    print "All set up and ready. Please run `epio django createsuperuser` to"
    print "create a superuser to log in and go to %s.ep.io to add some pages!" % appname

if __name__ == '__main__':
    main()