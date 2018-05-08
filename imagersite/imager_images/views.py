"""Image Views."""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from django.contrib.auth.models import User
from django.views.generic import ListView


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
        'profile': profile,
        'albums': albums,
        'photos': photos,
    }

    return render(request, 'imager_images/library.html', context)


class PhotoView(ListView):
    """Render public photos page."""

    template_name = 'imager_images/photo.html'
    context_object_name = 'photos'

    def get(self, *args, **kwargs):
        """Redirect home if user's not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Grab photo objects."""
        return Photo.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Grab contents for context."""
        context = super().get_context_data(**kwargs)

        return context


def album_view(request):
    """Show all public albums."""

    public_albums = Album.objects.filter(published='PUBLIC')

    context = {
        'public_albums': public_albums,
    }

    return render(request, 'imager_images/album.html', context)


def album_detail_view(request, id=None):
    """Show detail album."""
    this_album = Album.objects.filter(id=id).first()

    context = {
        'this_album': this_album,
    }

    return render(request, 'imager_images/album_detail.html', context)


def photo_view(request):
    """Define the library view."""
    public_photos = Photo.objects.filter(published='PUBLIC')

    context = {
        'public_photos': public_photos,
    }

    return render(request, 'imager_images/photo.html', context)


def photo_detail_view(request, id=None):
    """Define the library view."""
    this_photo = Photo.objects.filter(id=id).first()

    context = {
        'this_photo': this_photo,
    }

    return render(request, 'imager_images/photo_detail.html', context)
