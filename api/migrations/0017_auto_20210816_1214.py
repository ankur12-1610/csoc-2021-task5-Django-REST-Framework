# Generated by Django 3.2.6 on 2021-08-16 06:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0016_remove_collab_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collab',
            name='user',
        ),
        migrations.AddField(
            model_name='collab',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
