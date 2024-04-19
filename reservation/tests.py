from django.test import TestCase
from django.urls import reverse
from .models import Reservation
from .forms import ReserveTableForm

# Create your tests here.

class ReservationTestCase(TestCase):
    def setUp(self):
        self.reservation_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'number_of_persons': 4,
            'Date': '2024-04-04',
            'time': '18:00',
            'message': 'Test reservation',
        }

    def test_reservation_form_valid(self):
        form = ReserveTableForm(data=self.reservation_data)
        self.assertTrue(form.is_valid())

    def test_reservation_form_invalid(self):
        invalid_data = self.reservation_data.copy()
        invalid_data['phone'] = 'abc'
        form = ReserveTableForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_reserve_table_view(self):
        response = self.client.get(reverse('reserve_table'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation.html')

    def test_reservation_success_view(self):
        reservation = Reservation.objects.create(**self.reservation_data)
        response = self.client.get(reverse('reservation_success', args=[reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_success.html')
