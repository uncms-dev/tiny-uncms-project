#!/bin/sh
flake8 tiny_project
pylint tiny_project
isort --diff --check-only
