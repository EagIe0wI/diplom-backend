from django.urls import path
from . import views
from accounts.views import RegisterView, LoginView, LogOutView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", LogOutView.as_view(), name='logout'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]