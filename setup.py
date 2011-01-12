# -*- coding: utf-8 -*-
from __future__ import with_statement
import epiocms
import fnmatch
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

with open('README.rst', 'r') as fobj:
    long_desc = fobj.read()
    
media_files = []

for dirpath, dirnames, filenames in os.walk(os.path.join('epiocms', 'data', 'media')):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        failed = False
        for pattern in ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*'):
            if fnmatch.fnmatchcase(filename, pattern):
                failed = True
        if failed:
            continue
        media_files.append(os.path.join(*filepath.split(os.sep)[1:]))
    
setup(
    name='django-cms-epio-quickstart',
    version=epiocms.__version__,
    url='https://github.com/ojii/django-cms-epio-quickstart/',
    download_url='http://pypi.python.org/pypi/django-cms-epio-quickstart',
    license='BSD',
    author='Jonas Obrist',
    author_email='jonas.obrist@divio.ch',
    description='Quickstart command line app for the django CMS for ep.io',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    package_data={
        'epiocms': [
            'data/epio.ini',
            'data/requirements.txt',
            'data/urls.py',
            'data/settings.py',
            'data/templates/*.html',
        ]+ media_files,
    },
    entry_points={
        'console_scripts': [
            'epiocms = epiocms.main:main',
        ],
    },
)