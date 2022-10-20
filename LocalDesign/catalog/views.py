from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from catalog.forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
import datetime
from catalog.models import Application
from django.db.models import Q


class ApplicationAllListView(generic.ListView):
    model = Application
    template_name = 'index.html'
    paginate_by = 4

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
def delete_application(request, pk):
    application = Application.objects.filter(username=request.user, pk=pk, status='new')
    if application:
        application.delete()
    return redirect('profile')


class CreateAppView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['name', 'description', 'categories', 'image']
    template_name = 'createapp.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.date = datetime.date.today()
        return super().form_valid(form)


class ApplicationAdminView(generic.ListView):
    model = Application
    template_name = 'appadmin.html'
    paginate_by = 10

    def get_queryset(self):
        return Application.objects.filter(Q(status='done') | Q(status='in work')).order_by('-date')
