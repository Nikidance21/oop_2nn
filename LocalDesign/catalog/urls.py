from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('accounts/profile/', profile, name='profile'),
]
