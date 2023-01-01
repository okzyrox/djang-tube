from django.db import models
from django.contrib.auth.models import User

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