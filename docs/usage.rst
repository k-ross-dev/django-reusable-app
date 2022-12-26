=====
Usage
=====

To use Django reusable app in a project, add it to your `INSTALLED_APPS`:

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
