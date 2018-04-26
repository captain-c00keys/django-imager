"""Doc string."""
from django.test import TestCase
from .models import Album, Photo
from imager_profile.models import User
import factory
from random import choice


choices1 = (
            'PRIVATE',
            'SHARED',
            'PUBLIC'
)

choices2 = ('DSLR', 'M', 'AC', 'SLR')

choices3 = ['blackandwhite',
            'night',
            'marco',
            '3d',
            'artistic',
            'underwater']


class AlbumFactory(factory.django.DjangoModelFactory):
    """Dummy test for the Album."""

    class Meta:
        """Docstring for Meta Class."""

        model = Album

        title = factory.Faker('words')
        description = factory.Faker('sentences')
        user = factory.Faker('name')
        date_created = factory.Faker('past_date')
        date_modified = factory.Faker('past_date')
        date_published = factory.Faker('past_date')
        published = choice(choices1)


class PhotoFactory(factory.django.DjangoModelFactory):
    """Dummy test for Photo."""

    class Meta:
        """Docstring for Meta Class."""

        model = Photo

        album = factory.Faker('words')
        title = factory.Faker('words')
        description = factory.Faker('sentences')
        date_created = factory.Faker('past_date')
        date_modified = factory.Faker('past_date')
        date_published = factory.Faker('past_date')
        published = choice(choices1)


class UserFactory(factory.django.DjangoModelFactory):
    """Dummy test for the user."""

    class Meta:
        """Docstring for Meta Class."""

        model = User

        username = factory.Faker('user_name')
        email = factory.Faker('email')


class ProfileUnitTests(TestCase):
    """Dummy test for the profile."""

    @classmethod
    def setUpclass(cls):
        """Create user, album and photo data."""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            album = AlbumFactory.create(user=user)
            album.save()

            photo = PhotoFactory.create(user=user)
            photo.save()

        @classmethod
        def tearDownClass(cls):
            """To tear down database."""
            super(TestCase, cls)
            User.objects.all().delete()
            Photo.objects.all().delete()
            Album.objects.all().delete()

        def test_album_title(self):
            """Test to see user profile."""
            one_album = Album.objects.first()
            self.assertIsNotNone(one_album.title)
