from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default = 'My blog ')
    header_image = models.ImageField(null=True, blank=True,upload_to="images/")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    #body=models.TextField()
    body=RichTextField(blank=True, null=True)
    category =models.CharField(max_length=255, default ='coding')
    post_date = models.DateField(auto_now_add=True)
    likes= models.ManyToManyField(User, related_name ='blog_post')
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    



class ProfileModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    profile_pic = models.ImageField(null=True,blank=True, upload_to ="images/")
    facebook = models.CharField(max_length=100 ,null=True,blank=True)
    twitter = models.CharField(max_length=100,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    linkedin = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return str(self.user)