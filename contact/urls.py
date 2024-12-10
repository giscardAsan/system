from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('action/', views.action, name='action'),
    path('crime/', views.crime, name='crime'),
    path('documentary/', views.documentary, name='documentary'),
    path('drama/', views.drama, name='drama'),
    path('hollywood/', views.hollywood, name='hollywood'),
    path('horror/', views.horror, name='horror'),
    path('kids/', views.kids, name='kids'),
    path('recommended/', views.recommended, name='recommended'),
    path('romantic/', views.romantic, name='romantic'),
    path('tv_shows/', views.tv_shows, name='tv_shows'),
]
