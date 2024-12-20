from django.shortcuts import render
from cart.models import Cart
from .models import Product



# class ProductList(ListView):
#     model = Product
#     template_name = "product/shop.html"
#     context_object_name = "product"


# class ProductDetail(DetailView):
#     model = Product
#     template_name = "product/show.html"
#     context_object_name = "product"


# def productDetail2(request, product_id):
#     product = Product.objects.get(id=product_id)
#     imageModel = ""
#     product_info = ""

#     if ProductImage.objects.filter(product=product).count():
#         imageModel = ProductImage.objects.filter(product=product).get()

#     if ProductInfo.objects.filter(product=product).count():
#         product_info = ProductImage.objects.filter(product=product).get()

#     relatedProduct = Product.objects.raw('SELECT * FROM product_product WHERE  name  LIKE  %s limit 2', [product.name])

    # relatedProduct = Product.objects.filter(name=product.name)
    #     print(pro)
    # context = {"def_product": product, "imagelist": imageModel, 'related': relatedProduct, 'product_info': product_info}
    # return render(request, "product/show.html", context)
     
    
def product_list(request):
    phones = Product.objects.all()
    # laptop = Product.objects.filter(name="laptop")
    # Tv = Product.objects.filter(name="Tv")
    # context = {"Phone": phones, "Laptop": laptop, "Tv": Tv}
    # return render(request, "product/product_list.html", {'phone': phones})

    if request.user.is_authenticated:
        Added_cart = Cart.objects.filter(user=request.user).count()
        request.session['cart'] = Added_cart
        request.session.modified = True
        return render(request, "product/product_list.html", {'phone': phones})
    else:

        request.session['cart'] = 0
        return render(request, "product/product_list.html", {'phone': phones})
    
    
def search_venues(request):
   if request.method == "POST":
      searched = request.POST['searched']
      products = Product.objects.filter(name__contains=searched)
      
      return render(request, "product/search_venues.html", {
         'searched':searched,
         'products':products
         })
   else:
      return render(request, 'product/search_venues.html', {})
    
    
def Product_Detail(request, product_id):
    ProductDetails = Product.objects.get(id = product_id)
    
    # relatedproduct = Product.objects.filter( related=ProductDetails.related).get()
    
    relatedProduct = Product.objects.raw('SELECT * FROM product_product WHERE  brand  LIKE  %s limit 5', [ProductDetails.brand])
    
    return render(request, "product/Product_Detail.html", {
        
    "ProductDetail": ProductDetails, 
    "relatedProduct": relatedProduct, 
    
    })
        