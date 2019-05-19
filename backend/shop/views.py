from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        content = {}
        return render(request, 'home.html')
        

class LoginView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'registration/login.html'
        logout(request)
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            template_name = 'home.html'
            login(request, user)
            return render(request, template_name, {'user': user})
        else:
            template_name = 'registration/login.html'
            return render(request, template_name, {'error': "Please try again!"})


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/register.html')

    def post(self, request, *args, **kwargs):
        _username = request.POST.get('username')
        _lastname = request.POST.get('lastname')
        _firstname = request.POST.get('firstname')
        _email = request.POST.get('email')
        _password = request.POST.get('pass')
        user = User.objects.create_user(username=_username, email=_email, password=_password)
        user.first_name = _firstname
        user.last_name = _lastname
        if user is not None: 
            user.save()
            print(user)
            group = Group.objects.get(name='customer')
            group.user_set.add(user)
            logout(request)
            return redirect('shop:login')
        else:
            return render(request, 'registration/register.html')






class LogoutView(View):
    def get(self, request, *args, **kwargs):
        return redirect('shop:login')
        # return render(request, template_name, {'logout':"logout success!"})


class CartView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'cart.html'
        return render(request, template_name)