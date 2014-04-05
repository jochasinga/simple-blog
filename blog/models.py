from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    """Database model for posting on blog"""
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        """Prettify the name of the instance when queried upon"""
        return self.title
    
    class Meta:
        """Reverse-chronologically ordered post.
           Omit the '-' to do it in ascending order"""
        ordering = ('-timestamp',)


