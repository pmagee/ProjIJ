from django.test import TestCase
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from vouchers.models import Voucher
from order.models import Order, OrderItem, Feedback

# testing order model
class OrderModelTestCase(TestCase):
    def setUp(self):
        self.voucher = Voucher.objects.create(
            code='TESTVOUCHER',
            valid_from=timezone.now(),
            valid_to=timezone.now() + timezone.timedelta(days=30),
            discount=10,
            active=True
        )

    def test_order_with_voucher(self):
        order = Order.objects.create(
            token='test_token',
            total=80.00,
            emailAddress='test@example.ie',
            billingName='Test',
            billingAddress1='123 Test Lawn',
            billingCity='Test City',
            billingPostcode='12345',
            billingCountry='Test Country',
            shippingName='Test Shipping Name',
            shippingAddress1='789 Test Way',
            shippingCity='Shipping City',
            shippingPostcode='23456',
            shippingCountry='Shipping Country',
            voucher=self.voucher,
            discount=10
        )
    
    def test_order_without_voucher(self):
        order = Order.objects.create(
            token='test_token',
            total=80.00,
            emailAddress='test@example.ie',
            billingName='Test',
            billingAddress1='123 Test Lawn',
            billingCity='Test City',
            billingPostcode='12345',
            billingCountry='Test Country',
            shippingName='Test Shipping Name',
            shippingAddress1='789 Test Way',
            shippingCity='Shipping City',
            shippingPostcode='23456',
            shippingCountry='Shipping Country',
            discount=0 
        )

        self.assertEqual(order.total, 80.00)

    def test_order_with_invalid_voucher(self):
        expired_voucher = Voucher.objects.create(
            code='INVALIDVOUCHER',
            valid_from=timezone.now() - timezone.timedelta(days=30),
            valid_to=timezone.now() - timezone.timedelta(days=1),
            discount=10,
            active=False
        )

# testing orderItem model
class OrdeItemModelTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            token='test_token',
            total=80.00,
            emailAddress='test@example.ie',
            billingName='Test',
            billingAddress1='123 Test Lawn',
            billingCity='Test City',
            billingPostcode='12345',
            billingCountry='Test Country',
            shippingName='Test Shipping Name',
            shippingAddress1='789 Test Way',
            shippingCity='Shipping City',
            shippingPostcode='23456',
            shippingCountry='Shipping Country',
            discount=0 
        )

    def test_sub_total_calculation(self):
        item = OrderItem.objects.create(
            food='Sushi',
            quantity=5,
            price=10.00,
            order=self.order
        )

        self.assertEqual(item.sub_total(), 50.00)

    def test_order_item_return_string(self):
        item = OrderItem.objects.create(
            food='Sushi',
            quantity=5,
            price=10.00,
            order=self.order
        )

        self.assertEqual(str(item), 'Sushi')    

# testing Feedback (review) model
class FeedbackModelTestCase(TestCase):
    def test_feedback_return_string(self):
        feedback = Feedback.objects.create(
            customer_name='Test',
            feedback_text='testing...',
            rating=5
        )

        expected_string = 'Test | 5/5'
        self.assertEqual(str(feedback), expected_string)    