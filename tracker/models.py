from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

# Create your models here.
class Client(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, related_name='projects')

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.client.name)

class TimeEntry(TimeStampedModel):
    project = models.ForeignKey(Project, related_name='time_entries')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='time_entries')
    hours = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{2} - {0} - {1}h'.format(self.user.get_full_name(), self.hours, self.project)