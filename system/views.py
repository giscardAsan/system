from django.shortcuts import render

from product.models import Product



def main(request):
    context = {"key": "Your welcome! "}
    return render(request, 'main.html', context)

def watch(request):
    return render(request, 'next.html')

def backend(request):
   return render(request, 'backend1-1.html')

def new(request):
   return render(request, 'new.html')

def africa(request):
    return render(request, 'africa.html')
 
def comedy(request):
   return render(request, 'comedy.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
def new(request):
   return render(request, 'new.html')
 
def backend(request):
   return render(request, 'backend1-1.html')

def upcoming(request):
   return render(request, 'upcoming.html')

def talent(request):
   return render(request, 'talent.html')


def policy(request):
   return render(request, 'policy.html')

