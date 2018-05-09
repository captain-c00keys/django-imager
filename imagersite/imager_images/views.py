"""Image Views."""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class LibraryView(ListView):
    """Render library page."""

    template_name = 'imager_images/library.html'
    context_object_name = 'library'
    
    def get(self, *args, **kwargs):
        """Retrieve keyword args."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Filter object."""
        # import pdb; pdb.set_trace()
        photos = Photo.objects.filter(user__username=self.request
                                      .user.username)
        albums = Album.objects.filter(user__username=self.request
                                      .user.username)

    def get_context_data(self, **kwargs):
        """Pass context objects."""
        context = super().get_context_data(**kwargs)
        import pdb; pdb.set_trace()
        context['albums'] = context['library']
        context['photos'] = context['library']
        del context['library']

        return context
    


# def library_view(request):
#     """Handle library view request."""
#     # import pdb; pdb.set_trace()
#     username = request.user.get_username()

#     if username == '':
#         return redirect('home')
#     profile = get_object_or_404(User, username=username)
#     photos = Photo.objects.filter(user__username=username)
#     albums = Album.objects.filter(user__username=username)

#     context = {
#         'profile': profile,
#         'albums': albums,
#         'photos': photos,
#     }

#     return render(request, 'imager_images/library.html', context)


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


class AddPhoto(CreateView):
    """Add photo."""

    template_name = 'imager_images/add_photo.html'
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    form_class = AddPhotoForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """If form is valid, save, assign user and re-direct."""
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


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


class AddAlbum(CreateView):
    """Add photo."""

    template_name = 'imager_images/add_album.html'
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """If form is valid, save, assign user and re-direct."""
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)
