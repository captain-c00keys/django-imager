"""Image Profile Views."""

from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from .models import ImagerProfile


def profile_view(request, username=None):
    """Render codes for profile."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    # import pdb; pdb.set_trace()
    profile = get_object_or_404(ImagerProfile, user__username=username)

    albums = Album.objects.filter(user__username=username)
    albums_public = albums.filter(published='PUBLIC')
    albums_private = albums.filter(published='PRIVATE')

    photos = Photo.objects.filter(album__user__username=username)
    photos_public = photos.filter(published='PUBLIC')
    photos_private = photos.filter(published='PRIVATE')

    if not owner:
        photos_public = Photo.objects.filter(published='PUBLIC')
        photos_private = 'None'
        albums_public = Album.objects.filter(published='PUBLIC')
        albums_private = 'None'

    context = {
        'profile': profile,
        'photos_public': photos_public,
        'photos_private': photos_private,
        'albums_public': albums_public,
        'albums_private': albums_private,
    }

    return render(request, 'imager_profile/profile.html', context)
