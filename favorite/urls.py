from django.urls import path
from . import views




urlpatterns = [

    path("add-favorite/<int:product_id>", views.Add_Favorite, name='Add_Favorite'), 
    
    path("Show_Favorite/", views.Show_Favorite, name="Show_Favorite"),
    
    path("Delete_favorite/<int:product_id>", views.Delete_Favorite, name="Delete_Favorite"),
    

]