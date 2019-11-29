from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.CharField(max_length=100)

class Topic(models.Model):
  subject = models.CharField(max_length=255)
  last_updated = models.DateTimeField(auto_now_add=True)
  board = models.ForeignKey(Board, on_delete=-models.CASCADE, related_name='topics')
  starter = models.ForeignKey(user, on_delete=models.CASCADE, related_name='topics')
# board = models.ForeignKey(Board, related_name='topics')
# starter = models.ForeignKey(User, related_name='topics')

class Post(models.Model):
  message = models.TextField(max_length=4000)
  topic = models.ForeignKey(Topic, on_deleted=models.CASCADE, related_name='posts') 
# topic = models.ForeignKey(Topic, related_name='posts')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True)
  updated_by = models.ForeignKey(User, related_name='posts')
  updated_by = models.ForeignKey(User, null=True, related_name='+')


