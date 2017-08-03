from django.db import models
from django.utils import timezone


class Post(models.Model):                           # defining a Django model called "Post"
    author = models.ForeignKey('auth.User')         # defining a property of Post, "ForeignKey" refers to another model
    title = models.CharField(max_length=200)        # CharField = text field with limited length
    text = models.TextField()                       # TextField = unlimited text field
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):                              # defining a method (action) for Post called "publish", needs to be indented bc part of the class definition
        self.published_date = timezone.now()
        self.save()

    def __str__(self):                              # gives out the title as a string
        return self.title

