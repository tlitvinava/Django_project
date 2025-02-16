from .views import ProductsViewSet, CategoriesViewSet  # Импортируем представления для продуктов и категорий
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')  # Регистрация маршрутов для продуктов
router.register(r'categories', CategoriesViewSet, basename='categories')  # Регистрация маршрутов для категорий

urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты из маршрутизатора
]
