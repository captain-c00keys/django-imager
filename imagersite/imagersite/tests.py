"""Tests for app login."""

from django.test import TestCase


class LoginTest(TestCase):
    """Inital testing for login and regristration."""

    def test_login(self):
        """Test for successful login."""
        self.client  # client fpr testing requests

        response = self.client.post(
            '/accounts/login/',
            {'username': 'tester2', 'password': 'code@1234'})
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Test login page loads from login route."""
        self.client
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.template_name[0], 'registration/login.html')

    def test_home_page(self):
        """Test message renders with home page route."""
        self.client
        response = self.client.get('/')
        self.assertEqual(response.context[-1]['message'], 'Hello World')

    def test_registration_page(self):
        """Test login page renders with registration route."""
        self.client
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.template_name[0],
                         'registration/registration_form.html')
