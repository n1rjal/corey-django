from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#user,posts

#1st lets make a post model
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    #picture=models.ImageField(name="image",null=True,blank=True,upload_to="image")
    author=models.ForeignKey(User,on_delete=models.CASCADE)