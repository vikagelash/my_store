from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register_user'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='user_profile'),
    path('update/<int:user_id>/', views.UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:user_id>/', views.DeleteUserView.as_view(), name='delete_user'),
]
