from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from custom_user.admin import UserCreationForm




# Create your views here.



def index(request):
    context = {"key": "I am at Home "}
    return render(request, "app/home.html", context)


class CustomLoginView(LoginView):
    template_name = "app/login.html"
    fields = "__all__"
    redirect_app_user = True

    def get_success_url(self):
        return reverse_lazy('home')



class CustomRegisterView(FormView):
    template_name = "app/register.html"
    form_class = UserCreationForm
    redirect_app_user = True
    success_url = reverse_lazy("home") # Automatically redirect to homepage after Registration

    def form_valid(self, form):
        user = form.save()  # Automatically Save Registering User
        if user is not None:
            login(self.request, user)  # Automatically log us in
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")  # Prevent User Registeration form from showing
        return super(CustomRegisterView, self).get(request, *args, **kwargs)




