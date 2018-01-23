from rest_framework.generics import(
	ListAPIView, 
	RetrieveAPIView, 
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView,
	)
from restaurants.models import Restaurant, Item
from .serializers import(
	RestaurantListSerializer,
	RestaurantDetailSerializer, 
	RestaurantCreateUpdateSerializer,
	ItemDetailSerializer,
	ItemListSerializer,
	)
from rest_framework.permissions import( 
	 AllowAny,
	 IsAuthenticated, 
	 IsAdminUser,
	 )
from rest_framework.filters import SearchFilter


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all().order_by('-name')
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated]

class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all().order_by('-created')
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'id'
	permission_classes = [IsAuthenticated, IsAdminUser]

class RestaurantCreateView(CreateAPIView):
	queryset = Restaurant.objects.all().order_by('-created')
	serializer_class = RestaurantCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]
	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)


class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all().order_by('-created')
	serializer_class = RestaurantCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'id'
	permission_classes = [IsAuthenticated, IsAdminUser]    

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated]



	

		
