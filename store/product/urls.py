from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),  # All products
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),  # Single product detail
    path('add/', views.AddProductView.as_view(), name='add_product'),  # Add new product
    path('update/<int:pk>/', views.UpdateProductView.as_view(), name='update_product'),  # Update existing product
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),  # Delete product
]
