#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn mysite.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=mysite.settings \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=debug \
    # --log-file=/tmp/gs_gunicorn.log \
    # --access-logfile=/tmp/gs_gunicorn_access.log
