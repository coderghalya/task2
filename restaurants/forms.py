from django import forms
from .models import Restaurant, Item

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'logo', 'description']



class ItemForm(forms.ModelForm):
	class Meta:
		model = Item 
		fields = ['restaurant', 'name', 'description', 'price']       
        