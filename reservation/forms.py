from django import forms
from .models import Reservation, Table

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'number_of_persons', 'date', 'time', 'message', 'tables']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tables'].queryset = Table.objects.filter(is_available=True)

    def clean(self):
        cleaned_data = super().clean()
        selected_tables = cleaned_data.get("tables")
        number_of_persons = cleaned_data.get("number_of_persons")
        if selected_tables.exists() and number_of_persons:
            selected_table = selected_tables.first()
            if number_of_persons > selected_table.capacity:
                raise forms.ValidationError(
                    f"This table can accommodate up to {selected_table.capacity} people."
                )
        return cleaned_data

    def save(self, commit=True):
        reservation = super().save(commit=False)
        selected_table = self.cleaned_data.get('tables')
        if selected_table:
            selected_table_instance = selected_table.first()
            selected_table_instance.is_available = False  # Set table as unavailable
            selected_table_instance.save()
        if commit:
            reservation.save()
        return reservation
