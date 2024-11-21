from django.urls import path
from . import views




product_name = 'product'

urlpatterns = [
    path("Product_Detail/<int:product_id>", views.Product_Detail, name="Product_Detail"),
    path("product_list/", views.product_list, name="product_list"),
    path('search_value', views.search_value, name="search-value"),

] 