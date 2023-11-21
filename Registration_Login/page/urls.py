from django.urls import path
from . import views
from .views import home,register,login_user,logout_user



urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path("login_user",views.login_user,name="login_user"),
     path("logout_user",views.logout_user,name="logout_user")
]


