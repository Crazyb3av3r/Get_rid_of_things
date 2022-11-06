from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.functional import lazy
from django.views import View
from django.views.generic import CreateView, FormView, RedirectView
from django.views.generic.base import TemplateResponseMixin

from .forms import UserAdminCreationForm, LoginForm
from .models import CustomUser


# Create your views here.
User = get_user_model()


class UserCreateView(CreateView):
    """
    View for creating a new object, with a response render by a template.
    """
    model = CustomUser
    template_name = 'register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    permission_required = None

    def form_valid(self, form):

        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['password1'])
        self.object.save()
        print(self.object)
        return response


class LoginView(FormView):
    template_name = "app/login.html"
    success_url = reverse_lazy('home')
    form_class = LoginForm

    def form_valid(self, form):
        """If the form is valid and user was authenticated, redirect to the user home page"""
        user = form.user
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, redirect to the Registration URL"""
        return redirect('register')


class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=1)
        return render(request, 'app/profile.html', {'user': user})

# class LoginView(View):
#     form_class = LoginForm
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, 'app/login.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )
#             email = form.cleaned_data['email']
#             user_info = CustomUser.objects.get(email=email)
#             context = {'user': user_info, 'test': 'testowy', 'username': user.first_name, 'form': form}
#             return render(request, 'app/index.html', context)
