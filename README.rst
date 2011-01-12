###########################
django CMS ep.io quickstart
###########################

An easy way to get the django CMS up and running on ep.io.

************
Installation
************

* ``pip install -e git+https://github.com/ojii/django-cms-epio-quickstart.git#egg=django-cms-epio-quickstart``

.. note:: I highly recommend installing this in a virtualenv!

************
Requirements
************

* Python 2.5 or higher.
* epio client.
* ep.io account.

*****
Usage
*****

.. note:: In this tutorial I assume you are on a Unix based system.

Substitute words wrapped in ``<>`` signs with sensible values.

* ``cd <workspace>``
* ``mkdir <appname>``
* ``cd myepiocms``
* ``epio create <appname>``
* ``epiocms``
* ``epio django createsuperuser``
* Open your ``http://<appname>.ep.io`` in a browser.