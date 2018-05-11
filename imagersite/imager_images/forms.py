"""Definition for forms."""

from .models import Album, Photo
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, widgets, TextField


class AlbumEditForm(ModelForm):
    """Definition for album edit form."""

    name = CharField(
        max_length=Album._meta.get_field('name').max_length,
        required=False)

    description = TextField(required=False)

    published = CharField(
        max_length=Album._meta.get_field('published').max_length,
        required=False)

    class Meta:
        """."""

        model = Album
        fields = ['photos', 'name', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """."""
        id = kwargs.pop('id')
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = Album.objects.get(id=id).name
        self.fields['description'].initial = User.objects.get(id=id).description
        self.fields['published'].initial = User.objects.get(id=id).published
