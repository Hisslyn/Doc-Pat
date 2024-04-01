from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import register
from .views import list_doctors

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),  
    path('doctors/', list_doctors, name='doctor_list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),  
    path('doctors/<int:doctor_id>/book/', views.book_time_slot, name='book_time_slot'),  
    path('booking/success/', views.booking_success_view, name='booking_success'),  
    path('booking/error/', views.booking_error, name='booking_error'),  
    path('', views.home_view, name='home'),
]


