from django.urls import path
from restaurant import views 
from .views import SignUpView, ProfileEditView

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    # edit profile url 
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
]
