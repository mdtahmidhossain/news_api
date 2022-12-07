from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    url_to_image = models.URLField(max_length=255, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)


class Source(models.Model):
    api_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    article = models.ManyToManyField(Article)
