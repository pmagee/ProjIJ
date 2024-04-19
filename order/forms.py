from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['customer_name', 'feedback_text', 'rating']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)])  # Dropdown menu with choices 1 to 5
        }