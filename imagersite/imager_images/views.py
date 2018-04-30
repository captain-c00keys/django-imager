"""Image Views."""

from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from django.contrib.auth.models import User


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


def image_album_view(request, album_id=None):
    """Render codes for profile."""
    if album_id:
        # display an appropriately sized rendering of the photo, perhaps with a lightbox feature to show the full-sized image. It should also display any metadata available about the photo
        albums = Album.objects.filter(id=album_id).all()

    else:
        # display all the public photos
        albums = Photo.objects.filter(published='PUBLIC').all()

    context = {
        'albums': albums
    }

    return render(request, 'imager_images/images.html', context)


def library_view(request):
    """Handle library view request."""
    # import pdb; pdb.set_trace()
    username = request.user.get_username()

    if username == '':
        return redirect('home')
    profile = get_object_or_404(User, username=username)
    photos = Photo.objects.filter(user__username=username)
    albums = Album.objects.filter(user__username=username)

    context = {
        'photos': photos,
        'albums': albums,
        'username': username,
        'profile': profile
    }

    return render(request, 'imager_images/library.html', context)


def image_detail_photo_view(request):
    """Filter out id from photos."""
    image_detail = Photo.object.filter(id=id).first()

    context = {
        'image_detail': image_detail
    }

    return render(request, 'imager_images/image_photo_detail', context)


def image_detail_album_view(request):
    """Filter out id from albums."""
    album_detail = Album.object.filter(id=id).first()

    context = {
        'album_detail': album_detail
    }

    return render(request, 'imager_images/image_album_detail', context)

# def image_one_photo(request, photo_id=None):
#     """Render codes for profile."""
#     return render(request, 'imager_images/images.html')