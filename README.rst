===================
Django reusable app
===================

Your project description goes here


.. image:: https://img.shields.io/pypi/v/django-reusable-app.svg
        :target: https://pypi.python.org/pypi/django-reusable-app

.. image:: https://img.shields.io/travis/Used to initialize GIT repo origin remote/django-reusable-app.svg
        :target: https://travis-ci.org/Used to initialize GIT repo origin remote/django-reusable-app

.. image:: https://readthedocs.org/projects/django-reusable-app/badge/?version=latest
        :target: https://django-reusable-app.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/Used to initialize GIT repo origin remote/django-reusable-app/badge.svg?branch=develop
        :target: https://coveralls.io/github/Used to initialize GIT repo origin remote/django-reusable-app?branch=develop
        :alt: Coveralls.io coverage

.. image:: https://codecov.io/gh/Used to initialize GIT repo origin remote/django-reusable-app/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/Used to initialize GIT repo origin remote/django-reusable-app
        :alt: CodeCov coverage

.. image:: https://api.codeclimate.com/v1/badges/0e7992f6259bc7fd1a1a/maintainability
        :target: https://codeclimate.com/github/Used to initialize GIT repo origin remote/django-reusable-app/maintainability
        :alt: Maintainability

.. image:: https://img.shields.io/github/license/Used to initialize GIT repo origin remote/django-reusable-app.svg
        :target: https://github.com/Used to initialize GIT repo origin remote/django-reusable-app/blob/develop/LICENSE
        :alt: License

.. image:: https://img.shields.io/twitter/url/https/github.com/Used to initialize GIT repo origin remote/django-reusable-app.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/Used to initialize GIT repo origin remote/django-reusable-app
        :alt: Tweet about this project

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
        :target: https://saythanks.io/to/Used to initialize GIT repo origin remote


* Free software: MIT license
* Documentation: https://django-reusable-app.readthedocs.io.

Features
--------

* Pending :D

Demo
----

To run an example project for this django reusable app, click the button below and start a demo serwer on Heroku

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
    :alt: Deploy Django Opt-out example project to Heroku


Quickstart
----------

Install Django reusable app::

    pip install django-reusable-app

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_reusable_app.apps.DjangoReusableAppConfig',
        ...
    )

Add Django reusable app's URL patterns:

.. code-block:: python

    from django_reusable_app import urls as django_reusable_app_urls


    urlpatterns = [
        ...
        url(r'^', include(django_reusable_app_urls)),
        ...
    ]


Running Tests
-------------

Does the code actually work?

::

    $ pipenv install --dev
    $ pipenv shell
    $ tox


We recommend using pipenv_ but a legacy approach to creating virtualenv and installing requirements should also work.
Please install `requirements/development.txt` to setup virtual env for testing and development.


Credits
-------

This package was created with Cookiecutter_ and the `wooyek/cookiecutter-django-app`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`wooyek/cookiecutter-django-app`: https://github.com/wooyek/cookiecutter-django-app
.. _`pipenv`: https://docs.pipenv.org/install#fancy-installation-of-pipenv
