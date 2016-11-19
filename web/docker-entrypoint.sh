#!/bin/bash
python manage.py migrate    # Apply database migrations

exec gunicorn config.wsgi:application \
    --name ksupcapp \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    "$@"
