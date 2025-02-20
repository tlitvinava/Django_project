from .views import ProductsViewSet, CategoriesViewSet  # Импортируем представления для продуктов и категорий
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from hello import views
from .views import product

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')  # Регистрация маршрутов для продуктов
router.register(r'categories', CategoriesViewSet, basename='categories')  # Регистрация маршрутов для категорий

#router.register(r'categories_overview', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты из маршрутизатора
    path('category_overview', product),
    # path("", views.index),
    # path("product/", views.user)
]
