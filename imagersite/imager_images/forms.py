"""Definition for forms."""

from .models import Album, Photo
from django.contrib.auth.models import User
from django.forms import ModelForm


class AlbumForm(ModelForm):
    """Definition for album edit form."""

    class Meta:
        """."""

        model = Album
        fields = ['cover', 'name', 'description', 'published', 'photos']

    def __init__(self, *args, **kwargs):
        """."""
        username = kwargs.pop('username')
        # import pdb; pdb.set_trace()
        super().__init__(*args, **kwargs)
        self.fields['photos'].queryset = Photo.objects.filter(
            user__username=username)
        self.fields['cover'].queryset = Photo.objects.filter(
            user__username=username)
