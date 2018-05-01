"""Shows the Album and Photo database setup."""
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Album(models.Model):
    """Database makeup for Albums."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='albums')
    cover = models.ForeignKey(
        'Photo',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True)

    photos = models.ManyToManyField('Photo', related_name='albums')
    name = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=10,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        """User representaion of name."""
        return '{}'.format(self.name)


class Photo(models.Model):
    """Database makeup for Photos."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='photos')
    image = ImageField(upload_to='images', null=False, blank=False)
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=10,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        """User representation of title."""
        return '{}'.format(self.title)