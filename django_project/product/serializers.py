from rest_framework import serializers
from .models  import*

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Categories
        fields = "__all__"  

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta():
        model = Products
        fields = "__all__"


      