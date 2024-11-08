from django.shortcuts import render



def main(request):
    context = {"key": "Your welcome! "}
    return render(request, 'main.html', context)