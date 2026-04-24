from django.urls import path
# from . import views
from tasks.views import RegisterView, LoginView, LogOutView

app_name = 'accounts'

urlpatterns = [
    # path("", RegisterView.as_view(), name='register'),
    # path("", LoginView.as_view(), name='login'),
    # path("", LogOutView.as_view(), name='logout'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile_view, name='profile'),
]