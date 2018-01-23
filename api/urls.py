from django.urls import path 
from .views import RestaurantListView, RestaurantDetailView, RestaurantDeleteView, RestaurantCreateView, RestaurantUpdateView, ItemDetailView

urlpatterns = [
	path('list/', RestaurantListView.as_view(), name="api-list"),
	path('detail/<int:id>/', RestaurantDetailView.as_view(), name="api-detail"),
	path('delete/<int:id>/', RestaurantDeleteView.as_view(), name="api-delete"),
	path('update/<int:id>/', RestaurantUpdateView.as_view(), name="api-update"),
	path('create/', RestaurantCreateView.as_view(), name="api-create"),
	path('itemdetail/<int:id>/', ItemDetailView.as_view(), name="api-itemdetail"),
]