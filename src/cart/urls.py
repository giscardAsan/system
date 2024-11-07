from django.urls import path

from . import views




urlpatterns = [

    path("add-cart/<int:product_id>", views.Add_Cart, name='Add_Cart'),
    path("Show_Cart/", views.Show_Cart, name="Show_Cart"),
    path("Update_Cart/<int:product_id>", views.Update_Cart, name="Update_Cart"),
    path("Delete_Cart/<int:product_id>", views.Delete_Cart, name="Delete_Cart"),
    path("list", views.list, name="list_cart")

]