# Generated by Django 2.2.5 on 2019-09-14 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]
