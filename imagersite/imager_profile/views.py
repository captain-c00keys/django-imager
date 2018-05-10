"""Image Profile Views."""

from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from .models import ImagerProfile
from django.contrib.auth.models import User
from django.views.generic import DetailView


# def profile_view(request, username=None):
#     """Render codes for profile."""
#     owner = False

#     if not username:
#         username = request.user.get_username()
#         owner = True
#         if username == '':
#             return redirect('home')

#     # import pdb; pdb.set_trace()
#     profile = get_object_or_404(ImagerProfile, user__username=username)

#     albums = Album.objects.filter(user__username=username)
#     albums_public = albums.filter(published='PUBLIC')
#     albums_private = albums.filter(published='PRIVATE')

#     photos = Photo.objects.filter(user__username=username)
#     photos_public = photos.filter(published='PUBLIC')
#     photos_private = photos.filter(published='PRIVATE')

#     if not owner:
#         photos_public = Photo.objects.filter(published='PUBLIC')
#         photos_private = 'None'
#         albums_public = Album.objects.filter(published='PUBLIC')
#         albums_private = 'None'

#     context = {
#         'profile': profile,
#         'photos_public': photos_public,
#         'photos_private': photos_private,
#         'albums_public': albums_public,
#         'albums_private': albums_private,
#     }

#     return render(request, 'imager_profile/profile.html', context)
  
class ProfileView(DetailView):
    """Render a profile page."""

    template_name = 'imager_profile/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'
    model = ImagerProfile

    # def get(self, *args, **kwargs):
    #     """Retrieve keyword args."""
    #     if not self.request.user.is_authenticated:
    #         return redirect('home')

    #     return super().get(*args, **kwargs)

    # def get_queryset(self):
    #     """Filter object."""
    #     import pdb; pdb.set_trace()
    #     owner = False

    #     username = self.request.user.username
    #     if username:
    #         owner = True

    #     photos = Photo.objects.filter(user__username=self.request.user.username)
    #     photos_public = photos.objects.filter(published='PUBLIC')
    #     photos_private = photos.objects.filter(published='PRIVATE')

    #     albums = Album.objects.filter(user__username=self.request.user.username)
    #     albums_public = albums.objects.filter(published='PUBLIC')
    #     albums_private = albums.objects.filter(published='PRIVATE')
    #     # import pdb; pdb.set_trace()

    #     if not owner:
    #         photos_public = Photo.objects.filter(published='PUBLIC')
    #         photos_private = 'None'
    #         albums_public = Album.objects.filter(published='PUBLIC')
    #         albums_private = 'None'

    #     return photos_public, photos_private, albums_public, albums_private

    def get_context_data(self, **kwargs):
        """Obtain profile context."""

        context = super().get_context_data(**kwargs)
        username = context['profile'].user.username

        # import pdb; pdb.set_trace()

        photos = Photo.objects.filter(user__username=username)
        photos_public = photos.filter(published='PUBLIC')
        photos_private = photos.filter(published='PRIVATE')

        albums = Album.objects.filter(user__username=username)
        albums_public = albums.filter(published='PUBLIC')
        albums_private = albums.filter(published='PRIVATE')

        context['photos_public'] = photos_public
        context['photos_private'] = photos_private,
        context['albums_public'] = albums_public,
        context['albums_private'] = albums_private
        context['photos_public_count'] = photos_public.count()
        context['photos_private_count'] = photos_private.count()
        context['albums_public_count'] = albums_public.count()
        context['albums_private_count'] = albums_public.count()

        # del context['profile']
        return context
