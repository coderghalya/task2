from django.contrib import admin
from django.urls import path

from restaurants import views

urlpatterns = [
   path('list/', views.restaurant_list, name="restaurant_list"),
   path('detail/<int:restaurant_id>/', views.restaurant_detail, name="restaurant_detail"),
   path('create/',views.restaurant_create, name='restaurant_create'),
   path('update/<int:restaurant_id>/',views.restaurant_update, name='restaurant_update'),
   path('delete/<int:restaurant_id>/',views.restaurant_delete, name='restaurant_delete'),  
   path('item_create/<int:restaurant_id>/',views.restaurant_create, name='item_create'),

   ]