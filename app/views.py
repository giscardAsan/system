from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import FormView
from custom_user.admin import UserCreationForm
from verify_email.email_handler import send_verification_email



def main(request):
    context = {"key": "Your welcome! "}
    return render(request, 'app/main.html', context)

def watch(request):
    return render(request, 'app/next.html')

def backend(request):
   return render(request, 'app/backend1-1.html')

def new(request):
   return render(request, 'app/new.html')

def africa(request):
    return render(request, 'app/africa.html')
 
def comedy(request):
   return render(request, 'app/comedy.html')

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')
 
def new(request):
   return render(request, 'app/new.html')
 
def backend(request):
   return render(request, 'app/backend1-1.html')

def upcoming(request):
   return render(request, 'app/upcoming.html')

def talent(request):
   return render(request, 'app/talent.html')


def policy(request):
   return render(request, 'app/policy.html')

def index(request):
    context = {"key": "I am at Home "}
    return render(request, "app/home.html", context)






inactive_user = 'app'

def send_welcome_email(request):
        subject = 'Welcome To My Site'
        massage = 'Thank you for creating an account!'
        from_mail = 'admin@Mysite.com'
        global inactive_user
        recepient_list = [inactive_user]
        send_mail(subject,massage,from_mail,recepient_list)
        return redirect("main")


# def register_user(request):
#     ...
#     if form.is_valid():

#         inactive_user = send_verification_email(request, form)
#         inactive_user.cleaned_data['email']

        # Output: test-user123@gmail.com



class CustomLoginView(LoginView):
    template_name = "app/login.html"
    fields = "__all__"
    redirect_app_user = True

    def get_success_url(self):
         if self.request.method == "POST":
            try:
                remember_me = str(self.request.POST['checkbox'])
                if remember_me: 
             # This if statement can change, 
             # but the purpose is checking remember me checkbox is checked or not.
                   self.request.session.set_expiry(86400 * 28) # Here we extend session.
                   print("Check")

            except:
                   # This part of code means, close session when browser is closed.
                   self.request.session.set_expiry(28) 
                   print("UnCheck")


         else:
             # GET method
             if self.request.user.is_authenticated: 
                print(" Remember ME !!!!")
         return reverse_lazy('main')



class CustomRegisterView(FormView):
    template_name = "app/register.html"
    form_class = UserCreationForm
    redirect_app_user = True
    success_url = reverse_lazy("send_welcome_email") # Automatically redirect to homepage after Registration
    inactive_user = ''

    def form_valid(self, form):
        # user = form.save()  # Automatically Save Registering User
        global inactive_user
        inactive_user = send_verification_email(self.request, form) 
        form.cleaned_data['email']
        if inactive_user is not None:
            login(self.request, inactive_user)  # Automatically log us in
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("main")  # Prevent User Registeration form from showing
        return super(CustomRegisterView, self).get(request, *args, **kwargs)




