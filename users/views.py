from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.views import View


class RegisterFormView(FormView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = "/dashboard/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Rejestracja zakończona sukcesem!')
        return super().form_valid(form)

class LoginFormView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = "/dashboard/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Zalogowano')
        return super().form_valid(form)


class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(self.request, 'Wylogowano')
        return redirect('login')
