# Generated by Django 4.1.2 on 2023-01-01 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoGameTopicGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=250)),
                ('game_desc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='videoTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='videoObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('video_title', models.CharField(max_length=250)),
                ('video_description', models.TextField(blank=True, max_length=500, null=True)),
                ('rawvideo', models.FileField(null=True, upload_to='media/usercontent/video/', verbose_name='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('video_creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('video_gametopic_game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.videogametopicgame')),
                ('video_topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.videotopic')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]