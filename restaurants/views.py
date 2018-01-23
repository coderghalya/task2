from django.shortcuts import render, redirect
import random
from .models import Restaurant, Item
from .forms import RestaurantForm, ItemForm
from django.shortcuts import redirect
from django.http import Http404

# Create your views here.
def restaurant_list(request):
    object_list= Restaurant.objects.all().order_by("name")
    info = {
            "feed": object_list
    }
    return render(request, 'restaurant_list.html', info)

def restaurant_detail(request, restaurant_id):      
    thing = Restaurant.objects.get(id=restaurant_id)
    item_list= Item.objects.filter(restaurant=thing)  
    context = {
        "thing":thing,
        "item_list": item_list,
    }
    return render(request, 'restaurant_detail.html', context)

def restaurant_create(request):
    if not (request.user.is_staff):
        raise Http404 
    form = RestaurantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        form.save()
        return redirect("restaurant_list")

    context = {
    "form": form,
    }
    return render(request, 'restaurant_create.html', context)   

 
def restaurant_update(request, restaurant_id):
    if not (request.user.is_staff):
        raise Http404 
    instance = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_id=instance.id)
        if form is is_valid():
            form.save()
            return redirect("restaurant_list")

    context = {
    "form":form,
    "instance": instance,
    }
    return render(request, 'restaurant_update.html', context)   

def restaurant_delete(request, restaurant_id):
    if not (request.user.is_staff):
         raise Http404 
    instance = Restaurant.objects.get(id=restaurant_id)
    instance.delete()
    return redirect("restaurant_list") 

def item_create(request, restaurant_id):
    restaurant= Restaurant.objects.get(id=restaurant_id)
    
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        item.restaurant-restaurant
        form.save()
        return redirect("restaurant_detail", restaurant_id=restaurant.id)

    context = {
    "restaurant": restaurant,
    "form": form,
    }
    return render(request, 'item_create.html', context)   

 
def item_update(request, item_id):
    
    instance = Item.objects.get(id=restaurant_id)
    form = ItemForm(request.POST or None,  instance = instance)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_id=instance.id)


    context = {
    "form":form,
    "instance": instance,
    }
    return render(request, 'restaurant_update.html', context)   

def restaurant_delete(request, restaurant_id):
    if not (request.user.is_staff):
         raise Http404 
    instance = Restaurant.objects.get(id=restaurant_id)
    instance.delete()
    return redirect("restaurant_list")
