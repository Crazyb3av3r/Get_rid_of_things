from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic.base import TemplateResponseMixin

from .forms import UserAdminCreationForm, LoginForm
from .models import CustomUser


# Create your views here.
User = get_user_model()


class UserCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new object, with a response render by a template.
    """
    model = CustomUser
    template_name = 'register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    permission_required = 'auth.add_user'

    def form_valid(self, form):

        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['password1'])
        self.object.save()
        print(self.object)
        return response


class LoginView(FormView):
    template_name = "app/login.html"
    success_url = reverse_lazy('login-user-page')
    form_class = LoginForm

    def form_valid(self, form):
        """If the form is valid and user was authenticated, redirect to the user home page"""
        user = form.user
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, redirect to the Registration URL"""
        return redirect('register')
