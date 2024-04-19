from django.urls import path
from contactform.views import contact, success

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
]