from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import User
from .forms import UserForm
from .serializers import UserSerializer

class RegisterUserView(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'register_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False
            request.session['user_id'] = user.id
            return redirect('user_profile', user_id=user.id)
        return render(request, 'register_user.html', {'form': form})

class UserProfileView(APIView):
    def get(self, request, user_id):
        session_user_id = request.session.get('user_id')
        if session_user_id != user_id:
            return redirect('user_profile', user_id=session_user_id)
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return render(request, 'user_profile.html', {'user': serializer.data})

class UpdateUserView(APIView):
    def get(self, request, user_id):
        session_user_id = request.session.get('user_id')
        if session_user_id != user_id:
            return redirect('user_profile', user_id=session_user_id)

        user = get_object_or_404(User, id=user_id)
        form = UserForm(instance=user)
        return render(request, 'update_user.html', {'form': form})

    def post(self, request, user_id):
        session_user_id = request.session.get('user_id')
        if session_user_id != user_id:
            return redirect('user_profile', user_id=session_user_id)

        user = get_object_or_404(User, id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=user.id)
        return render(request, 'update_user.html', {'form': form})

# Delete User View
class DeleteUserView(APIView):
    def get(self, request, user_id):
        session_user_id = request.session.get('user_id')
        if session_user_id != user_id:
            return redirect('user_profile', user_id=session_user_id)

        user = get_object_or_404(User, id=user_id)
        return render(request, 'delete_user.html', {'user': user})

    def post(self, request, user_id):
        session_user_id = request.session.get('user_id')
        if session_user_id != user_id:
            return redirect('user_profile', user_id=session_user_id)

        user = get_object_or_404(User, id=user_id)
        user.delete()
        request.session.flush()
        return redirect('register_user')
