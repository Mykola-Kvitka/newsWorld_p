from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topic(models.Model):
    tittle=models.CharField(max_length=50)
    creationDate=models.DateField()
    def __str__(self):
        return self.tittle


class News(models.Model):
    name = models.CharField(max_length=200)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.DateField()
    writer = models.CharField(max_length=100)
    show = models.BooleanField(default=False)   # default=0 for integer field-when i use this in existing models
    topicId=models.ManyToManyField(Topic, help_text="Select a topick for this news")
    def __str__(self):
            return self.name

class Member(models.Model):
    name = User.first_name
    username = User.username  ## utxt for username
    email = User.email
    ip = models.TextField(default="") # Get User IP Address
    time = models.TimeField(default="")

class Comment(models.Model):
    authorName=models.TextField()
    commentBody=models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    newsId=models.IntegerField(default=0)
    def __str__(self):
            return self.authorName

    