"""User and profile test."""
from django.test import TestCase
from .models import ImagerProfile, User
import factory
from random import choice


choices = (('DSLR', 'Digital Single Lens Reflex'), ('M', 'Mirrorless'),
           ('AC', 'Advanced Compact'),
           ('SLR', 'Single Lens Reflex'))
choices1 = ["('DSLR', 'Digital Single Lens Reflex')",
            "('M', 'Mirrorless')",
            "('AC', 'Advanced Compact')",
            "('SLR', 'Single Lens Reflex')"]
choices2 = [('blackandwhite', 'Black and White'),
            ('night', 'Night'),
            ('marco', 'Macro'),
            ('3d', '3D'),
            ('artistic', 'Artistic'),
            ('underwater', 'Underwater')]


class UserFactory(factory.django.DjangoModelFactory):
    """Dummy test for the user."""

    class Meta:
        """Docstring for Meta Class."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    """Dummy test for the profile."""

    class Meta:
        """Docstring for Meta Class."""

        model = ImagerProfile

    bio = factory.Faker('sentence')
    phone = factory.Faker('phone_number')
    location = factory.Faker('street_address')
    website = factory.Faker('uri')
    fee = factory.Faker('pyint')
    camera = choice(choices)
    services = choice(choices1)
    photostyles = choice(choices2)


class ProfileUnitTests(TestCase):
    """Unit testing for profile."""

    @classmethod
    def setUpClass(cls):
        """Create class for testing user."""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

    @classmethod
    def tearDownClass(cls):
        """Take down database after test."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        """Tests if user can see profile."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)
