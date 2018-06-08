from django.shortcuts import render
from rest_framework import generics
from .serializers import PhotoSerializer
from imager_images.models import Photo


class PhotoListApi(generics.ListAPIView):
    """Photo list API."""

    serializer_class = PhotoSerializer

    def get_queryset(self):
        """Get all photo objects."""
        return Photo.objects.filter(user=self.request.user)