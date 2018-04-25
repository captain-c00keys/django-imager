from django.test import TestCase
from .models import Album, Photo
import factory
from random import randint, choice


choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public')
)


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    title = factory.Faker('title')
    description = factory.Faker('description')
    user = factory.Faker('user')
    description = factory.Faker('description')
    date_created = factory.Faker('date_created')
    date_modified = factory.Faker('date_modified')
    date_published = factory.Faker('date_published')
    published = factory.Faker('published')

class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    album = factory.Faker('album')
    title = factory.Faker('title')
    description = factory.Faker('description')
    date_created = factory.Faker('date_created')
    date_modified = factory.Faker('date_modified')
    date_published = factory.Faker('date_published')
    published = factory.Faker('published')


class ProfileUnitTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        for _ in range(50):
            user = AlbumFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            profile = ProfileFactory.create(user=user)
            profile.save()

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)
