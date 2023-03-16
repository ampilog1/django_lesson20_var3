from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy, reverse
from rest_framework.authtoken.models import Token
from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import BlogUser


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')


class UserDetailView(DetailView):
    template_name = 'userapp/profile.html'
    model = BlogUser


def update_token(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        # создать
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))
