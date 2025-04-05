from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.select_product_view, name='select_all_products'),
    path('products/<int:pk>/', views.select_product_view, name='select_one_product'),
    path('products/add/', views.add_product_view, name='add_product'),
    path('products/update/<int:pk>/', views.update_product_view, name='update_product'),
    path('products/delete/<int:pk>/', views.delete_product_view, name='delete_product'),


]
