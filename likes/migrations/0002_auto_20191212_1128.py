# Generated by Django 2.0 on 2019-12-12 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likerecord',
            old_name='uesr',
            new_name='user',
        ),
    ]
