from django.db import models


# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=128)
	logo = models.ImageField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	opening_time = models.DateTimeField(auto_now=True)
	closing_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
		
class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=7, decimal_places=3)
	
	def __str__(self):
		return self.name