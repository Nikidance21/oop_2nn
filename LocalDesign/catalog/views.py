from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from catalog.forms import RegisterUserForm
from django.contrib.auth.decorators import login_required

from catalog.models import Application


class ApplicationAllListView(generic.ListView):
    model = Application
    template_name = 'index.html'

    def get_queryset(self):
        return Application.objects.filter(status='done').order_by('-date')


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class ApplicationListView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'profile.html'

    def get_queryset(self):
        return Application.objects.filter(username=self.request.user).order_by('-date')


@login_required
def createapp(request):
    return render(request, 'createapp.html')


@login_required
def delete_application(request, pk):
    application = Application.odjects.filter(username=request.username, pk=pk, status='new')
    if application:
        application.delete()
    return redirect('applications')


#class CreateAppView(CreateView):
   # template_name = 'createapp.html'
    #form_class = CreateAppForm
  #  success_url = reverse_lazy('profile')
