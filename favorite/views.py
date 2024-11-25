from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from product.models import Product
from .models import Favorite
# Create your views here.







   
def like(request):
    return render(request, 'favorite/like.html')
                      # Add_Favorite
def Add_Favorite(request, product_id):
    if request.user.is_authenticated:
        # Using  product_id to get the exact product
        products = Product.objects.get(id=product_id)

        # Create a new cart in the cart Table
        Added_favorite, done = Favorite.objects.get_or_create(product=products, user=request.user)
        Added_favorite.quantity = 1
        Added_favorite.save()

        # Retrieve The number of cart related to a particular user

        Added_favorite = Favorite.objects.filter(user=request.user).count()

        # Save cart Count to a session
        request.session['favorite'] = Added_favorite
        request.session.modified = True
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    else:

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


                #   Show_Favorite
 
def Show_Favorite(request):
    if request.user.is_authenticated:

        favorite = Favorite.objects.filter(user=request.user)

        # MyQuantityRange = ""

        total = sum(item.Total_cost() for item in favorite)
        
        totall = sum(item.Total_costs() for item in favorite)

        # for cartdat in cart:
        #     MyQuantityRange = range(cartdat.product.quantity)
        # print(MyQuantityRange)

        context = {"favorite": favorite, "total": total, "totall": totall}

        return render(request, "favorite/like.html", context)

    else:
        context = {"UnregistedUserCart": "Pending"}

        return render(request, "favorite/like.html", context)
    
    
    
    
def Delete_Favorite(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        favorite = Favorite.objects.filter(product=product)
        favorite.delete()
        # Retrieve The number of cart related to a particular user
        Added_favorite = Favorite.objects.filter(user=request.user).count()

        # Save cart Count to a session
        request.session['favorite'] = Added_favorite
        request.session.modified = True
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
