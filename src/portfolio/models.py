from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
