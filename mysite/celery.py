# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os

from celery import Celery

from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
# Using a string here means the worker will not have to
# serialize the configuration object to child processes.
# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'UTC'

from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every 60 seconds
    'add-every-minute': {
        'task': 'tasks.add',
        'schedule': 1.0,
        'args': (16, 16),
    },
}

