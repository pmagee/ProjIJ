from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from .models import CustomUser

# testing custom user model in accounts app

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123',
            age=25
        )
        self.group = Group.objects.create(name='Test Group')
        self.permission = Permission.objects.get(name='Can add group')

    def test_custom_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password123'))
        self.assertEqual(self.user.age, 25)

    def test_user_groups(self):
        # Test adding groups to the user
        self.user.groups.add(self.group)
        self.assertIn(self.group, self.user.groups.all()) 

    def test_user_permissions(self):
        # Test adding permissions to the user
        self.user.user_permissions.add(self.permission)
        self.assertIn(self.permission, self.user.user_permissions.all())

    def test_blank_fields(self):
        # Test if blank fields are handled properly
        blank_user = CustomUser.objects.create_user(username='blankuser')
        self.assertIsNone(blank_user.age) 
