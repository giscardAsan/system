from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, 'contact/contact.html')

def action(request):
    return render(request, 'contact/action.html')

def crime(request):
    return render(request, 'contact/crime.html')

def document(request):
    return render(request, 'contact/document.html')

def drama(request):
    return render(request, 'contact/drama.html')

def hollywood(request):
    return render(request, 'contact/hollywood.html')

def horror(request):
    return render(request, 'contact/horror.html')

def kids(request):
    return render(request, 'contact/kids.html')

def recommend(request):
    return render(request, 'contact/recommend.html')

def romantic(request):
    return render(request, 'contact/romantic.html')

def tv_show(request):
    return render(request, 'contact/tv_show.html')