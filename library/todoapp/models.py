from uuid import uuid4

from django.db import models
from userapp.models import User


class Project(models.Model):
    class Meta:
        ordering = ["name"]

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, unique=True)
    repo_link = models.URLField(blank=True, null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TODO(models.Model):
    class Meta:
        ordering = ["-date_updated"]

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
