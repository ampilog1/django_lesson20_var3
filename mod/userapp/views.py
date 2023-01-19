from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView
from .forms import RegistrationForm
from django.views.generic import CreateView

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):

