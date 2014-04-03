from django.db import models


class BlogPost():
    """Model for posting on blog"""
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


