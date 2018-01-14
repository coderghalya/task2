from django.shortcuts import render
import random
from .models import Restaurant
from .forms import RestaurantForm
from django.shortcuts import redirect

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

def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
    "form": form,
    }
    return render(request, 'restaurant_create.html', context)	

 
 def restaurant_update(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_id=instance.id)
    context = {
    "form":form,
    "instance": instance,
    }
    return render(request, 'restaurant_update.html', context)   

 def restaurant_delete(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    instance.delete()
    return redirect("restaurant_list")   