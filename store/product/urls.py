from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add/', views.AddProductView.as_view(), name='add_product'),
    path('update/<int:pk>/', views.UpdateProductView.as_view(), name='update_product'),
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)