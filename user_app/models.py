from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class MyUser(AbstractUser):
    following = models.ManyToManyField(
        'self', related_name='follow', blank=True)
    avatar = models.ImageField(upload_to='static/i', null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)
    tags = TaggableManager()