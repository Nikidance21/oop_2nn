from django.urls import path
from . import views
from .views import createapp, ApplicationListView, delete_application, ApplicationAllListView


urlpatterns = [
    path('', ApplicationAllListView.as_view(), name='index'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('accounts/profile/', ApplicationListView.as_view(), name='profile'),
    path('accounts/profile/createapp/', createapp, name='createapp'),
    path(r'delete_application/<pk>', delete_application, name='delete_application')
]
