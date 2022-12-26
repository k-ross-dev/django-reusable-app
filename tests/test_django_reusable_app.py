#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `django-reusable-app` package."""

import pytest

import django_reusable_app


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/wooyek/cookiecutter-pylib')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_version_exists():
    """This is a stupid test dummy validating import of django_reusable_app"""
    assert django_reusable_app.__version__
