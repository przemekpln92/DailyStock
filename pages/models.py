from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,models.CASCADE)
	description = models.CharField(max_length=100,)
	city = models.CharField(max_length=100,)
	website = models.URLField()
	organisation = models.CharField(max_length=100,)
	phone = models.IntegerField()


class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, models.CASCADE)

		
