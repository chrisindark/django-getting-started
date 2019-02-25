from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        """Save model and if job is in pending state, schedule it"""
        instance = Job.objects.create(**validated_data)
        if instance.status in ('started', 'pending', 'failed', 'finished'):
            from .tasks import update_job
            update_job.delay(job_id=instance.id, n=instance.argument)

        return instance

    def update(self, instance, validated_data):
        """Save model and if job is in pending state, schedule it"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.status = 'started'
        instance.save()

        if instance.status in ('started', 'pending', 'failed', 'finished'):
            from .tasks import update_job
            update_job.delay(job_id=instance.id, n=instance.argument)

        return instance
