from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_product_view, name='product_list'),  # All products
    path('<int:pk>/', views.select_product_view, name='product_detail'),  # Single product detail
    path('add/', views.add_product_view, name='add_product'),  # Add product
    path('update/<int:pk>/', views.update_product_view, name='update_product'),  # Update product
    path('delete/<int:pk>/', views.delete_product_view, name='delete_product'),  # Delete product
]

