from django.urls import path
from passwordchange import views 
from . import views

urlpatterns = [
    path('change-password/', views.change_password,name='change_password'),
    path('password-success/', views.password_success,name='password_success'),
]
