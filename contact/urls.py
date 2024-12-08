from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('action/', views.action, name='action'),
    path('crime/', views.crime, name='crime'),
    path('document/', views.document, name='document'),
    path('drama/', views.drama, name='drama'),
    path('hollywood/', views.hollywood, name='hollywood'),
    path('horror/', views.horror, name='horror'),
    path('kids/', views.kids, name='kids'),
    path('recommend/', views.recommend, name='recommend'),
    path('romantic/', views.romantic, name='romantic'),
    path('tv_show/', views.tv_show, name='tv_show'),
]
