from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from .models import Donation, Institution, Category


def calculate_donations(obj):
    summ = 0
    for donation in obj:
        summ += donation.quantity
    return summ


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
        donations = Donation.objects.all()
        institutions_count = Institution.objects.all().count()
        sum_bugs = calculate_donations(donations)
        fundations = Institution.objects.filter(type=1)
        organizacje_pozarzadowe = Institution.objects.filter(type=2)
        zbiorki = Institution.objects.filter(type=3)
        context = {
            'sum_of_bugs': sum_bugs,
            'institutions_quantity': institutions_count,
            'organizacje_pozarzadowe': organizacje_pozarzadowe,
            'fundations': fundations,
            'zbiorki': zbiorki,
        }
        return render(request, 'app/index.html', context)


# @login_required
class AddDonation(View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'app/form.html', {'categories': categories,
                                                 'institutions': institutions
                                                 })
