# Generated by Django 3.0.5 on 2020-05-06 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
