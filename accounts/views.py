from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from django.utils.decorators import method_decorator
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated] # Только авторизованные пользователи видят это

#     def get(self, request):
#         return Response({"message": "Только авторизованные пользователи видят это"})

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = CustomUser.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({
            "status": "success registration",
            "user_id": user.pk
        })

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            
            return JsonResponse({
                "status": "success login",
                "user_id": user.pk
            })
        else:
            # Return an 'invalid login' error message.
            return JsonResponse({"status": "invalid login"})

class LogOutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({"status": "success logout"})

class ProfileView(View):
    def get(self, request):
        return JsonResponse({"status": "success profile"})
