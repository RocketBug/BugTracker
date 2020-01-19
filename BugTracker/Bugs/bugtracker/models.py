from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from projects.models import ProjectItem

class BugItem(models.Model):
    content = models.TextField(default="")
    content_type = models.TextField()
    content_title = models.TextField(default="None")
    content_description = models.TextField(default="None")
    content_time = models.DateTimeField(auto_now=True)
    #content_time = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectItem, on_delete=models.CASCADE) 

    class Meta:
        ordering = ['-content_time']