#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
pip install gunicorn
python manage.py collectstatic --no-input
python manage.py migrat