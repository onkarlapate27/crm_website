from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    # Registration
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'test_user',
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 302)

        # Verify user is created
        self.assertTrue(User.objects.filter(username='test_user').exists())

    def test_existing_username_registration(self):
        User.objects.create_user(username='existing_user', password='test_password')
        response = self.client.post(reverse('register'), {
            'username': 'existing_user',
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 302)

    # Login
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'test_user',
            'password': 'test_password',
        })
        self.assertEqual(response.status_code, 302)

    def test_user_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)