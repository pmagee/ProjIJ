from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'email','age', 'phone_number', 'address', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'email','age', 'phone_number', 'address',)


# Edit class 

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'address',)

 