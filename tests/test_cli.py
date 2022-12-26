#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `django-reusable-app` package."""

from click.testing import CliRunner

import django_reusable_app
from django_reusable_app import cli

django_reusable_app.__version__


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'django_reusable_app.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
