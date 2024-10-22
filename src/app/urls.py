from django.urls import path
from  .views import CustomLoginView
from .views import index
from  .views import CustomRegisterView
from django.contrib.auth.views import LogoutView








urlpatterns = [

     path("login/",CustomLoginView.as_view(),name="login"),
     path('', index, name="home"),
     path("register/",CustomRegisterView.as_view(),name="register"),
     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),


]


