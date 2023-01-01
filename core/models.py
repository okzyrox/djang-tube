from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class CreatorPost(models.Model):
    post_creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.post_title


class videoTopic(models.Model):
    topic_name = models.CharField(max_length=150)

    def __str__(self):
        return self.topic_name

class videoGameTopicGame(models.Model):
    game_name = models.CharField(max_length=250)
    game_desc = models.TextField(null=True)

    def __str__(self):
        return self.game_name


class videoObject(models.Model):
    video_uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)

    video_creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    video_title = models.CharField(max_length=250)
    video_description = models.TextField(max_length=500, null=True, blank=True)
    video_topic = models.ForeignKey(videoTopic, on_delete=models.SET_NULL, null=True)
    video_gametopic_game = models.ForeignKey(videoGameTopicGame, on_delete=models.SET_NULL, null=True)

    rawvideo = models.FileField(upload_to='video/', null=True, verbose_name="")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
