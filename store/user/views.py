# users/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

# List all users or detail one
def select_user_view(request, pk=None):
    if pk:
        user = get_object_or_404(User, pk=pk)
        return render(request, 'user_detail.html', {'user': user})
    else:
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})

# Add new user
def add_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('select_all_users')  # Assuming you have a URL named 'select_all_users'
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

# Update user
def update_user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('select_all_users')  # Redirect after successful update
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form, 'user': user})

# Delete user
def delete_user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('select_all_users')  # Redirect after successful deletion
    return render(request, 'delete_user.html', {'user': user})

# Optional: APIView for user-related API responses
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)
