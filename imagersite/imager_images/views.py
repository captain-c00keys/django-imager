"""Image Views."""

from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo


def image_view(request):
    """Render codes for profile."""
    return render(request, 'imager_images/images.html')


def image_photo_view(request, photo_id=None):
    """Render codes for profile."""
    if photo_id:
        # display an appropriately sized rendering of the photo, perhaps with a lightbox feature to show the full-sized image. It should also display any metadata available about the photo
        photos = Photo.objects.filter(id=photo_id).all()

    else:
        # display all the public photos
        photos = Photo.objects.filter(published='PUBLIC').all()

    context = {
        'photos': photos
    }

    return render(request, 'imager_images/images.html', context)


def image_one_photo(request, photo_id=None):
    """Render codes for profile."""
    return render(request, 'imager_images/images.html')


def library_view(request):
    """Handle library view request."""
    # import pdb; pdb.set_trace()
    username = request.user.get_username()
    photos = Photo.objects.filter(user__username=username)
    albums = Album.objects.filter(user__username=username)

    context = {
        'photos': photos,
        'albums': albums,
        'username': username
    }

    return render(request, 'imager_images/library.html', context)
