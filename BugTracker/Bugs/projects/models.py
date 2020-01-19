from django.db import models
from django.contrib.auth.models import User


class ProjectItem(models.Model):
    project_title = models.TextField()
    project_description = models.TextField()
    content_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-content_time']