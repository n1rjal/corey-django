# Generated by Django 3.0.5 on 2020-05-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='images/defaultimages.jpg', upload_to='images'),
        ),
    ]
