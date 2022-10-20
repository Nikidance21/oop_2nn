from django.urls import path
from . import views
from .views import ApplicationListView, delete_application, ApplicationAllListView, ApplicationAdminView

urlpatterns = [
    path('', ApplicationAllListView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/appadmin/', ApplicationAdminView.as_view, name='appadmin'),
    path('accounts/profile/', ApplicationListView.as_view(), name='profile'),
    path('accounts/profile/createapp/', views.CreateAppView.as_view(), name='createapp'),
    path(r'delete_application/<pk>', delete_application, name='delete_application')
]
