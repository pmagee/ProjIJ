from django.test import TestCase
from django.urls import reverse
from .models import Category, Food

# testing models in restaurant app

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Mexican',
            description='Tasty mexican cuisine'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Mexican')
        self.assertEqual(self.category.description, 'Tasty mexican cuisine')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Mexican' ,'Tasty mexican cuisine')

    def test_category_get_absolute_url(self):
        expected_url = reverse('restaurant:foods_by_category', args=[str(self.category.id)])
        self.assertEqual(self.category.get_absolute_url(), expected_url)

class FoodModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Mexican',
            description='Tasty mexican cuisine'
        )

        self.food = Food.objects.create(
            name='Nachos',
            description='Crunchy and creamy nachos',
            category=self.category,
            price=18.50,
            stock=15,
            available=True
        )

    def test_food_creation(self):
        self.assertEqual(self.food.name, 'Nachos')
        self.assertEqual(self.food.description, 'Crunchy and creamy nachos')
        self.assertEqual(self.food.category, self.category)
        self.assertEqual(self.food.price, 18.50)
        self.assertEqual(self.food.stock, 15)
        self.assertTrue(self.food.available)

    def test_food_str_method(self):
        self.assertEqual(str(self.food), 'Nachos')

    def test_food_get_absolute_url(self):
        expected_url = reverse('restaurant:food_detail', args=[str(self.category.id), str(self.food.id)])
        self.assertEqual(self.food.get_absolute_url(), expected_url)        
