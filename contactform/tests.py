from django.test import TestCase, Client
from django.urls import reverse
from contactform.forms import ContactForm

# Create your tests here.

class ContactFormTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)   

    def test_contact_view_post_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': '123456789',
            'subject': 'Test Subject',
            'message': 'Test Message',
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 302)

        last_submission = self.client.session.get('last_submission')
        self.assertIsNotNone(last_submission)
        self.assertIsInstance(last_submission, dict)
        self.assertEqual(last_submission['subject'], data['subject'])
        self.assertEqual(last_submission['message'], data['message'])

        response_success = self.client.get(reverse('success'))
        self.assertEqual(response_success.status_code, 200)
        self.assertTemplateUsed(response_success, 'success.html')
        self.assertEqual(response_success.context['last_submission']['subject'], data['subject'])
        self.assertEqual(response_success.context['last_submission']['message'], data['message'])


    def test_contact_view_post_invalid(self):
        data = {
            'name': '',
            'email': '',
            'phone': '',
            'subject': '',
            'message': '',
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone', form.errors)
        self.assertIn('subject', form.errors)
        self.assertIn('message', form.errors)
       
