from django.contrib import admin
from django.urls import path

from restaurants import views

urlpatterns = [
   path('list/', views.restaurant_list, name="url1"),
   path('detail/<int:restaurant_id>/', views.restaurant_detail, name="url2"),
   path('restaurant/create/',views.restaurant_create, name='restaurant_create'),
   path('restaurant/update/<int:restaurant_id>/',views.restaurant_update, name='restaurant_update'),
   path('restaurant/delete/<int:restaurant_id>/',views.restaurant_delete, name='restaurant_delete'),  
   ]