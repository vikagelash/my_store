# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.select_user_view, name='select_all_users'),  # List all users
    path('users/<int:pk>/', views.select_user_view, name='select_user'),  # User detail view
    path('users/add/', views.add_user_view, name='add_user'),  # Add new user
    path('users/update/<int:pk>/', views.update_user_view, name='update_user'),  # Update existing user
    path('users/delete/<int:pk>/', views.delete_user_view, name='delete_user'),  # Delete user
    path('api/users/', views.UserAPIView.as_view(), name='user_api'),  # API endpoint for users
]
