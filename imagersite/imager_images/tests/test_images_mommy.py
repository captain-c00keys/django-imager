
"""Test for integration."""

from django.test import TestCase
from imager_profile.models import User
from imager_images.models import Photo, Album
from model_mommy import mommy
import tempfile
import factory


class TestStoreRoutes(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)

        for n in range(10):
            user = mommy.make(User)
            user.set_password('password')
            user.save()
            album = mommy.make(Album, user=user)
            mommy.make(
                Photo,
                album=album,
                image=tempfile.NamedTemporaryFile(suffix='.png').name)

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        super(TestCase, cls)

    def test_200_status_on_authenticated_request_to_photos(self):
        import pdb; pdb.set_trace()
        user = User.objects.first()
        # self.client.login(username=user.username, password='password')
        self.client.force_login(user)
        response = self.client.get('/images/photos')
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_detail_photo(self):
        user = User.objects.first()
        photo = Photo.objects.first()
        self.client.force_login(user)
        response = self.client.get('/images/photos/{}'.format(photo.id))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    # def test_302_status_on_unauthenticated_request_to_product(self):
    #     product = Product.objects.first()
    #     response = self.client.get('/store/products/{}'.format(product.id))
    #     self.assertEqual(response.status_code, 302)

    def test_404_status_on_bad_request_to_photos(self):
        response = self.client.get('/images/photos/does_not_exist')
        self.assertEqual(response.status_code, 404)

    def test_302_status_on_unauthenticated_request_to_photo(self):
        response = self.client.get('/images/photos')
        self.assertEqual(response.status_code, 302)

    # def test_only_public_products_are_shown(self):
    #     user = User.objects.first()
    #     product = Product.objects.first()
    #     product.published = 'PUBLIC'
    #     product.save()

    #     self.client.force_login(user)
    #     response = self.client.get('/store/')
    #     self.client.logout()

    #     products = response.context['products']
    #     for prod in products:
    #         self.assertEqual(prod.published, 'PUBLIC')
