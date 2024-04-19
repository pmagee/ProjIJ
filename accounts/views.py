from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser

#Edit Code 
from .forms import CustomUserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.utils import timezone

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = form.cleaned_data.get('group')
            customer_group.customuser_groups.add(signup_user)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form })
        

# Edit Views 
        
class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        self.object.last_edit = timezone.now()
        self.object.save()
        return redirect(self.get_success_url())
        


