import django
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 
from . forms import CreateUserForm 
from django.contrib import messages
from django.contrib.auth.views import LoginView , LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

# Create your views here.

def register_user(request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"account created"+user)
            return redirect("/accounts/login/")
        else:
            print(form.errors)

    context = {"form":form}
    return render(request,"register.html",context)

@method_decorator(cache_control(no_cache=True, must_revalidate=True),name="dispatch")
class LoginUser(LoginView):
    template_name = "login.html"

 