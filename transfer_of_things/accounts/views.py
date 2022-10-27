from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserAdminCreationForm
from .models import CustomUser


# Create your views here.


class UserCreateView(PermissionRequiredMixin, CreateView):
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
