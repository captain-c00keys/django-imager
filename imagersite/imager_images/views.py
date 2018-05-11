"""Image Views."""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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
        return photos, albums

    def get_context_data(self, **kwargs):
        """Pass context objects."""
        context = super().get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        context['photos'] = context['library'][0]
        context['albums'] = context['library'][1]
        del context['library']

        return context


class PhotoView(ListView):
    """Render public photos page."""

    template_name = 'imager_images/photo.html'
    context_object_name = 'photos'
    queryset = Photo.objects.filter(published='PUBLIC')


class PhotoDetail(DetailView):
    """Render photo detail page."""

    template_name = 'imager_images/photo_detail.html'
    context_object_name = 'this_photo'
    model = Photo
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """Filter object."""
        return Photo.objects.filter(published='PUBLIC')


class AddPhoto(CreateView):
    """Add photo."""

    template_name = 'imager_images/add_photo.html'
    model = Photo
    # import pdb; pdb.set_trace()
    fields = ['image', 'title', 'description', 'published']
    # form_class = AddPhotoForm
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


class AlbumDetail(DetailView):
    """Render album detail page."""
    template_name = 'imager_images/album_detail.html'
    context_object_name = 'this_album'
    model = Album
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """Filter object."""
        return Album.objects.filter(published='PUBLIC')


class AddAlbum(CreateView):
    """Add photo."""

    # import pdb; pdb.set_trace()
    template_name = 'imager_images/add_album.html'
    model = Album
    # form_class = AddAlbumForm
    fields = ['user', 'cover', 'photos', 'name', 'published']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """If form is valid, save, assign user and re-direct."""
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class EditAlbum(LoginRequiredMixin, UpdateView):
    """Edit album."""

    template_name = 'imager_images/edit_album.html'
    model = Album
    # form_class = AlbumEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('library')
    slug_url_kwarg = 'id'
    slug_field = 'id'

    # def get(self, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    #     self.kwargs['username'] = self.request.user.get_username
    #     return super().get(*args, **kwargs)

    # def post(self, *args, **kwargs):
    #     self.kwargs['username'] = self.request.user.get_username
    #     return super().get(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs
    
    def form_valid(self, form):
        form.instance.user.email = form.data['email']
        form.instance.user.first_name = form.data['first_name']
        form.instance.user.last_name = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)

