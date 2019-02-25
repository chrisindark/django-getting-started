from django.db import models

# currently, available types of job are:
TYPES = (
    ('fibonacci', 'fibonacci'),
    ('power', 'power'),
)

# list of statuses that job can have
STATUSES = (
    ('pending', 'pending'),
    ('started', 'started'),
    ('finished', 'finished'),
    ('failed', 'failed'),
)


class Job(models.Model):
    """Class describing a computational job"""
    type = models.CharField(choices=TYPES, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    argument = models.PositiveIntegerField()
    result = models.IntegerField(null=True)
