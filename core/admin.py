from django.contrib import admin
from .models import CreatorPost, videoObject, videoTopic, videoGameTopicGame

# Register your models here.

admin.site.register(CreatorPost)
admin.site.register(videoObject)
admin.site.register(videoTopic)
admin.site.register(videoGameTopicGame)
