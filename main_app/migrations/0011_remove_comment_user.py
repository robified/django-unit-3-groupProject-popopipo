# Generated by Django 2.2.5 on 2019-09-15 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
