from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your password has been changed successfully......')
            return redirect('password_success')
    else:   
        form=PasswordChangeForm(request.user)
    return render (request,'change_password.html',{'form': form})


def password_success(request):
    return render(request, 'password_success.html', {})

