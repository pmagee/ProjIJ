from django.test import TestCase
from django.utils import timezone
from restaurant.models import Food, Category
from cart.models import Cart, CartItem
from django.urls import reverse
from django.test import Client
from accounts.models import CustomUser
import stripe


# Create your tests here.

class CartModelsTest(TestCase):
    def setUp(self):
        self.c = Category.objects.create(name='test category')
        self.food = Food.objects.create(
            name='Test Product',
            price=10.0,
            stock = 900,
            category=self.c
        )
        self.cart = Cart.objects.create(cart_id='test_cart', date_added=timezone.now())
        self.cart_item = CartItem.objects.create(
            food=self.food,
            cart=self.cart,
            quantity=2,
            active=True
        )

    def test_cart_str_method(self):
        self.assertEqual(str(self.cart), 'test_cart')

   
    def test_cart_item_str_method(self):
        expected_str = str(self.food)
        self.assertEqual(str(self.cart_item.food.name), expected_str)


class CartViewTests(TestCase):
    def setUp(self):
        self.c = Category.objects.create(name='test category')
        self.food = Food.objects.create(name='Test Product',
            price=10.0,
            stock=2,
            category=self.c,
        )

    def test_add_cart(self):
        response = self.client.get(reverse('cart:add_cart', args=[self.food.id]))
        self.assertEqual(response.status_code, 302)  
        cart = Cart.objects.get(cart_id=self.client.session.session_key)
        cart_item = CartItem.objects.get(food=self.food, cart=cart)
        self.assertEqual(cart_item.quantity, 1)

    def test_add_cart_quantity_limit(self):
        response = self.client.get(reverse('cart:add_cart', args=[self.food.id]))
        self.assertEqual(response.status_code, 302)  
        cart = Cart.objects.get(cart_id=self.client.session.session_key)
        cart_item = CartItem.objects.get(food=self.food, cart=cart)
        self.assertEqual(cart_item.quantity, 1)
        # Attempt to add more items than stock
        response = self.client.get(reverse('cart:add_cart', args=[self.food.id]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        cart_item.refresh_from_db()  # Refresh the cart_item instance
        self.assertEqual(cart_item.quantity, self.food.stock)
