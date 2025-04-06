from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user_view, name='register_user'),
    path('profile/<int:user_id>/', views.user_profile_view, name='user_profile'),  # User profile view
    path('update/<int:user_id>/', views.update_user_view, name='update_user'),  # Edit user profile
    path('delete/<int:user_id>/', views.delete_user_view, name='delete_user'),  # Delete user profile
]
