from django.shortcuts import render
import random
from .models import Restaurant

# Create your views here.
def restaurant_list(request):
	object_list= Restaurant.objects.all()
	info = {
			"feed": object_list
	}
	return render(request, 'restaurant_list.html', info)

def restaurant_detail(request, restaurant_id):
	thing = Restaurant.objects.get(id=restaurant_id)
	context = {
		"thing":thing
	}
	return render(request, 'restaurant_detail.html', context)