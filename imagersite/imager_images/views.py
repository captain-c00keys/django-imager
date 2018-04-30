"""Image Views."""

from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    """Handle library view request"""

    username = request.user.get_username()
    photos = Photo.objects.filter(user__username=username)
    albums = Album.objects.filter(user_username=username)

    album_page = request.GET.get("album_page", 1)
    photo_page = request.GET.get("photo_page", 1)

    album_pages = Paginator(albums, 2)
    photo_pages = Paginator(photos, 4)

    try:
        albums = album_pages.page(album_page)
        photos = photo_pages.page(photo_page)
    except PageNotAnInteger:
        albums = album_pages.page(1)
        photos = photo_pages.page(1)
    except EmptyPage:
        albums = album_pages.page(album_pages.num_pages)
        photos = photo_pages.page(photo_pages.num_pages)

    context = {
        'photos': photos,
        'albums': albums,
        'username': username,
    }

    return render(request, 'imager_images/library.html', context)


def album_view(request):
    """Show all public albums."""

    public_albums = Album.objects.filter(published='PUBLIC')

    context = {
        'public_albums': public_albums,
    }

    return render(request, 'imager_images/album.html', context)
