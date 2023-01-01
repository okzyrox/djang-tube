from django.forms import ModelForm
from .models import videoObject

class videoObjectCreationForm(ModelForm):
    class Meta:
        model=videoObject
        fields=['video_title', 'video_description', 'video_topic', 'rawvideo']
