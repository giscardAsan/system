from django.urls import path
from  .views import CustomLoginView, send_welcome_email
from .views import index
from  .views import CustomRegisterView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView






urlpatterns = [

     path("login/",CustomLoginView.as_view(),name="login"),
     path('', index, name="home"),
     path("register/",CustomRegisterView.as_view(),name="register"),
     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
     path('sen-welcome/', send_welcome_email, name='send_welcome_email'),
     path('accounts/login', CustomLoginView.as_view(), name='login'),
     path('login/', RedirectView.as_view(url='/accounts/login'), name='login'),
     path('login/', RedirectView.as_view(url='/admin'), name='login'),
]


