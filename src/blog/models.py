from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
