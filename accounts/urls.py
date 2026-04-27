from django.urls import path
from . import views
from accounts.views import RegisterView, LoginView, LogOutView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path("", views.RegisterView, name='register'),
    path("login/", views.LoginView, name='login'),
    path("logout/", LogOutView.as_view(), name='logout'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]