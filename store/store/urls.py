from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('products/', include('product.urls')),

    path('', lambda request: redirect('register_user'))
]
