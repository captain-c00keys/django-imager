"""Tests for app login."""

from django.test import TestCase
import factory
from django.contrib.auth.models import User


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


class ImagesRoutesTests(TestCase):
    """Class for testing views."""

    @classmethod
    def setUpClass(cls):
        """Test setup."""
        super(TestCase, cls)
        # fake = Faker()
        for _ in range(1):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for test."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_library_status(self):
        """Test library route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/library/')
        self.assertEqual(response.status_code, 200)

    def test_library_template(self):
        """Test library route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/library/')
        self.assertEqual(response.templates[0].name, 'imager_images/library.html')

    def test_library_base_template(self):
        """Test library route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/library/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_profile_status(self):
        """Test profile route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_template(self):
        """Test profile route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.templates[0].name, 'imager_profile/profile.html')

    def test_profile_base_template(self):
        """Test profile route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_profile_user_status(self):
        """Test profile route status code."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/{}'.format(user.username))
        self.assertEqual(response.status_code, 200)

    def test_profile_user_template(self):
        """Test profile route template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/{}'.format(user.username))
        self.assertEqual(
            response.templates[0].name, 'imager_profile/profile.html')

    def test_profile_user_base_template(self):
        """Test profile route base template."""
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get('/profile/{}'.format(user.username))
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_album_status(self):
        """Test album route status code."""
        response = self.client.get('/images/albums/')
        self.assertEqual(response.status_code, 200)

    def test_album_template(self):
        """Test album route template."""
        response = self.client.get('/images/albums/')
        self.assertEqual(response.templates[0].name, 'imager_images/album.html')

    def test_album_base_template(self):
        """Test album route base template."""
        response = self.client.get('/images/albums/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_photo_status(self):
        """Test photo route status code."""
        response = self.client.get('/images/photos/')
        self.assertEqual(response.status_code, 200)

    def test_photo_template(self):
        """Test photo route template."""
        response = self.client.get('/images/photos/')
        self.assertEqual(response.templates[0].name, 'imager_images/photo.html')

    def test_photo_base_template(self):
        """Test photo route base template."""
        response = self.client.get('/images/photos/')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_album_detail_status(self):
        """Test album_detail route status code."""
        response = self.client.get('/images/albums/1')
        self.assertEqual(response.status_code, 200)

    def test_album_detail_template(self):
        """Test album_detail route template."""
        response = self.client.get('/images/albums/1')
        self.assertEqual(
            response.templates[0].name, 'imager_images/album_detail.html')

    def test_album_detail_base_template(self):
        """Test album_detail route base template."""
        response = self.client.get('/images/albums/1')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_photo_detail_status(self):
        """Test photo_detail route status code."""
        response = self.client.get('/images/photos/1')
        self.assertEqual(response.status_code, 200)

    def test_photo_detail_template(self):
        """Test photo_detail route template."""
        response = self.client.get('/images/photos/1')
        self.assertEqual(
            response.templates[0].name, 'imager_images/photo_detail.html')

    def test_photo_detail_template_base(self):
        """Test photo_detail route base template."""
        response = self.client.get('/images/photos/1')
        self.assertEqual(response.templates[1].name, 'generic/base.html')