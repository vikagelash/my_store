from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def register_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_profile', user_id=user.id)  # Redirect to the profile page
    else:
        form = UserForm()
    return render(request, 'register_user.html', {'form': form})


def user_profile_view(request, user_id):
    user = User.objects.get(id=user_id)  # Get the user by ID
    return render(request, 'user_profile.html', {'user': user})

def update_user_view(request, user_id):
    user = User.objects.get(id=user_id)  # Get the user by ID
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=user.id)  # Redirect to the profile page after update
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})


def delete_user_view(request, user_id):
    user = User.objects.get(id=user_id)  # Get the user by ID
    if request.method == 'POST':
        user.delete()
        return redirect('register_user')  # Redirect to the homepage after deletion
    return render(request, 'delete_user.html', {'user': user})


