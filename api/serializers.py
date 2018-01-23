from rest_framework import serializers 
from restaurants.models import Restaurant, Item



class RestaurantListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name="api-detail", 
        lookup_field="id", 
        lookup_url_kwarg="id"
        )
    class Meta:
        model = Restaurant
        fields = ['name', 'logo', 'opening_time', 'closing_time', 'detail']


class RestaurantDetailSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'logo', 'opening_time', 'closing_time', 'item']  
        
    def get_item(self,obj):
        item_list = Item.objects.filter(restaurant=obj)
        return ItemListSerializer(item_list, many=True, context=self.context).data

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'logo', 'opening_time', 'closing_time']   

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name="api-itemdetail", 
        lookup_field="id", 
        lookup_url_kwarg="id"
        )
    class Meta:
        model = Item
        fields = ['name', 'detail', 'price']

class ItemDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Item
            fields = ['id', 'restaurant', 'name', 'description','price']


        