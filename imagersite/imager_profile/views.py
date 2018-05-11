"""Image Profile Views."""

from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from .models import ImagerProfile
from django.contrib.auth.models import User
from django.views.generic import DetailView


class ProfileView(DetailView):
    """Render a profile page."""

    template_name = 'imager_profile/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'
    model = ImagerProfile

    def get(self, *args, **kwargs):
        """Retrieve keyword args."""
        if 'username' not in kwargs:
            self.kwargs['username'] = self.request.user.username

        # import pdb; pdb.set_trace()
        return super().get(*args, **kwargs) 

    def get_context_data(self, **kwargs):
        """Obtain profile context."""
        context = super().get_context_data(**kwargs)
        username = context['profile'].user.username

        photos = Photo.objects.filter(user__username=username)
        photos_public = photos.filter(published='PUBLIC')
        photos_private = photos.filter(published='PRIVATE')

        albums = Album.objects.filter(user__username=username)
        albums_public = albums.filter(published='PUBLIC')
        albums_private = albums.filter(published='PRIVATE')

        context['photos'] = photos
        context['photos_public'] = photos_public
        context['photos_private'] = photos_private,
        context['albums_public'] = albums_public,
        context['albums_private'] = albums_private
        context['photos_public_count'] = photos_public.count()
        context['photos_private_count'] = photos_private.count()
        context['albums_public_count'] = albums_public.count()
        context['albums_private_count'] = albums_public.count()

        return context
