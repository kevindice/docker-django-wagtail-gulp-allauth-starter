#!/bin/bash
python manage.py migrate    # Apply database migrations

exec gunicorn manifest.wsgi:application \
    --name manifest \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    "$@"
