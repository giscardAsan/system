from django.urls import path
from . import views




product_name = 'product'

urlpatterns = [
    # path("product-list/", views.ProductList.as_view(), name="product-cart"),
    # path("product-detail/<int:product_id>", views.productDetail2, name="product"),
    # path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product"),
    path("product_list/", views.product_list, name="product_list"),

] 