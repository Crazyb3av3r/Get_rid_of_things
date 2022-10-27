from django.shortcuts import render
from django.views import View



class ShowPage(View):
    def get(self, request):
        return render(request, 'app/index.html')


class RegisterPage(View):
    def get(self, request):
        return render(request, 'app/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'app/index.html')


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'app/form-confirmation.html')
