from django.db import models

from manager.models import Manager


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    url = models.URLField(max_length=200)
    manager = models.ManyToManyField(Manager)


class Task(models.Model):
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
