from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
class RegisterView(View):
    def get(request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = CustomUser.objects.create_user(username=username, password=password)
        user.save()
        redirect(task_list)
        return JsonResponse({"status": "success registration"})

@csrf_exempt
class LoginView(View):
    def get(request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            redirect(task_list)
            return JsonResponse({"status": "success login"})
        else:
            # Return an 'invalid login' error message.
            return JsonResponse({"status": "invalid login"})

class LogOutView(View):
    def get(request):
        logout(request)
        return redirect('index')
        # Redirect to a success page.
