from django.urls import path
from  .views import CustomLoginView, send_welcome_email
from . import views
from  .views import CustomRegisterView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView






urlpatterns = [

     path("login/",CustomLoginView.as_view(),name="login"),
     path('', views.index, name="home"),
     path("register/",CustomRegisterView.as_view(),name="register"),
     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
     path('sen-welcome/', send_welcome_email, name='send_welcome_email'),
     path('accounts/login', CustomLoginView.as_view(), name='login'),
     path('login/', RedirectView.as_view(url='/accounts/login'), name='login'),
     path('login/', RedirectView.as_view(url='/admin'), name='login'),
     
     path('main/', views.main, name='main'),
     path('watch/', views.watch, name='watch'),
     path('backend/', views.backend, name="endd"),
     path('new/', views.new),
     path('talent/', views.talent),
     path('policy/', views.policy),
     path('backend/', views.backend, name="endd"),
     path('about/', views.about),
     path('comedy/', views.comedy, name="comedy"),
     path('africa/', views.africa, name="africa"),
     path('upcoming/', views.upcoming),
]


