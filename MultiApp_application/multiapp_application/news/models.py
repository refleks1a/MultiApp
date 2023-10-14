from django.db import models


class News(models.Model):
    author = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    urlToImage = models.URLField(blank=True, null=True)
    publishedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)