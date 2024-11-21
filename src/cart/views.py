from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from product.models import Product
from .models import Cart
# Create your views here.



def list(request):
    return render(request, 'cart/list.html')

def favorite(request):
    return render(request, 'cart/favorite.html')

def Add_Cart(request, product_id):
    if request.user.is_authenticated:
        # Using  product_id to get the exact product
        product = Product.objects.get(id=product_id)

        # Create a new cart in the cart Table
        Added_cart, done = Cart.objects.get_or_create(product=product, user=request.user)
        Added_cart.quantity = 1
        Added_cart.save()

        # Retrieve The number of cart related to a particular user

        Added_cart = Cart.objects.filter(user=request.user).count()

        # Save cart Count to a session
        request.session['cart'] = Added_cart
        request.session.modified = True
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    else:

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def Add_Favorite(request, product_id):
    if request.user.is_authenticated:
        # Using  product_id to get the exact product
        products = Product.objects.get(id=product_id)

        # Create a new cart in the cart Table
        Added_favorite, done = Cart.objects.get_or_create(product=products, user=request.user)
        Added_favorite.quantity = 1
        Added_favorite.save()

        # Retrieve The number of cart related to a particular user

        Added_favorite = Cart.objects.filter(user=request.user).count()

        # Save cart Count to a session
        request.session['favorite'] = Added_favorite
        request.session.modified = True
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    else:

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def Show_Cart(request):
    if request.user.is_authenticated:

        cart = Cart.objects.filter(user=request.user)

        # MyQuantityRange = ""

        total = sum(item.Total_cost() for item in cart)
        
        totall = sum(item.Total_costs() for item in cart)

        # for cartdat in cart:
        #     MyQuantityRange = range(cartdat.product.quantity)
        # print(MyQuantityRange)

        context = {"cart": cart, "total": total, "totall": totall}

        return render(request, "cart/list.html", context)

    else:
        context = {"UnregistedUserCart": "Pending"}

        return render(request, "cart/list.html", context)
 
def Show_Favorite(request):
    if request.user.is_authenticated:

        cart = Cart.objects.filter(user=request.user)

        # MyQuantityRange = ""

        total = sum(item.Total_cost() for item in cart)
        
        totall = sum(item.Total_costs() for item in cart)

        # for cartdat in cart:
        #     MyQuantityRange = range(cartdat.product.quantity)
        # print(MyQuantityRange)

        context = {"cart": cart, "total": total, "totall": totall}

        return render(request, "cart/favorite.html", context)

    else:
        context = {"UnregistedUserCart": "Pending"}

        return render(request, "cart/favorite.html", context)

 

def Update_Cart(request, product_id):
    if request.user.is_authenticated:
        # Using  product_id to get the exact product
        product = Product.objects.get(id=product_id)

        # Create a new cart in the cart Table
        Added_cart, done = Cart.objects.get_or_create(product=product, user=request.user)

        if int(request.POST['quantity']) <= 0 or product.quantity < (int(request.POST['quantity'])):
            Added_cart.quantity = 1
            Added_cart.save()
        else:
            Added_cart.quantity = request.POST['quantity']
            Added_cart.save()

        # Retrieve The number of cart related to a particular user

        Added_cart = Cart.objects.filter(user=request.user).count()

        # Save cart Count to a session
        request.session['cart'] = Added_cart
        request.session.modified = True
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    else:

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def Delete_Cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.filter(product=product)
        cart.delete()
        # Retrieve The number of cart related to a particular user
        Added_cart = Cart.objects.filter(user=request.user).count()

        # Save cart Count to a session
        request.session['cart'] = Added_cart
        request.session.modified = True
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))