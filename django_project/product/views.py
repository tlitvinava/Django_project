from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Products as Product
from .serializers import*
from .models import Products, Categories

from .serializers import ProductSerializer, CategorySerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
