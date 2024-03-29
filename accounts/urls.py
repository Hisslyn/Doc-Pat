from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import register
from .views import list_doctors

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register'),
    path('doctor_registration/', views.doctor_registration, name='doctor_registration_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('doctors/', list_doctors, name='doctor_list'),
    path('accounts/doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]

