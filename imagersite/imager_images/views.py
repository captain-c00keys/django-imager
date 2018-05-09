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
    queryset = Photo.objects.filter(published='PUBLIC')


class PhotoDetail(ListView):
    """Render photo detail page."""

    template_name = 'imager_images/photo_detail.html'
    context_object_name = 'this_photo'

    def get(self, *args, **kwargs):
        """Retrieve keyword args."""
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Filter object."""
        return Photo.objects.filter(id=self.kwargs['id']).first()


class AlbumView(ListView):
    """Render public albums page."""

    template_name = 'imager_images/album.html'
    context_object_name = 'public_albums'
    queryset = Album.objects.filter(published='PUBLIC')


class AlbumDetail(ListView):
    """Render album detail page."""

    template_name = 'imager_images/album_detail.html'
    context_object_name = 'this_album'

    def get(self, *args, **kwargs):
        """Retrieve keyword args."""
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Filter object."""
        return Album.objects.filter(id=self.kwargs['id']).first()
