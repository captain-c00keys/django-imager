"""Serializer file."""
from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Grab."""

    class Meta:
        """Get all metadata."""

        model = Photo
        fields = (
            'title',
            'image',
            'description',
            'date_created',
            'date_modified',
            'date_published')
