from django.shortcuts import render, redirect
from contactform.forms import ContactForm
from datetime import datetime

# Create your views here.

def contact(request):
    last_submission = request.session.get('last_submission')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['last_submission'] = {
                'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'last_submission': last_submission})

def success(request):
    last_submission = request.session.get('last_submission')
    if last_submission:
        return render(request, 'success.html', {'last_submission': last_submission})
    else:
        return render(request, 'contact', {})


