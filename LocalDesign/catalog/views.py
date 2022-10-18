from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from catalog.forms import RegisterUserForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


@login_required
def profile(request):
    return render(request, 'profile.html')
