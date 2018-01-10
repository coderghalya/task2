from django.db import models


# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=128)
	discription= models.TextField(null=True, blank=True)
	opening_time= models.DateTimeField(auto_now=True)
	closing_time= models.DateTimeField(auto_now_add=True)