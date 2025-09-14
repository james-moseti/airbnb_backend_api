#!/usr/bin/env bash
python manage.py migrate --noinput
exec gunicorn doc_project.wsgi:application --bind 0.0.0.0:$PORT
