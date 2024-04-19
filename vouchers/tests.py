from django.test import TestCase
from django.utils import timezone
from .models import Voucher

# testing voucher model in vouchers app

class VoucherModelTest(TestCase):
    @classmethod
    def setUp(cls):
        Voucher.objects.create(
            code='TESTVOUCHER20',
            valid_from=timezone.now(),
            valid_to=timezone.now(),
            discount=20,
            active=True
        )

    def test_voucher_code(self):
        voucher = Voucher.objects.get(id=1)
        field_label = voucher._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'code')

    def test_valid_from(self):
        voucher = Voucher.objects.get(id=1)
        field_label = voucher._meta.get_field('valid_from').verbose_name
        self.assertEqual(field_label, 'valid from')

    def test_valid_to(self):
        voucher = Voucher.objects.get(id=1)
        field_label = voucher._meta.get_field('valid_to').verbose_name
        self.assertEqual(field_label, 'valid to')

    def test_discount(self):
        voucher = Voucher.objects.get(id=1)
        field_label = voucher._meta.get_field('discount').verbose_name
        self.assertEqual(field_label, 'discount')

    def test_is_active_or_not(self):
        voucher = Voucher.objects.get(id=1)
        field_label = voucher._meta.get_field('active').verbose_name
        self.assertEqual(field_label, 'active')  
        