"""Home view."""

from django.shortcuts import render
from imager_images.models import Photo
from random import choice
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Render a homepage."""

    template_name = 'generic/home.html'

    def get_context_data(self, **kwargs):
        """Obtain photo context."""
        context = super().get_context_data(**kwargs)
        photos = Photo.objects.filter(published='PUBLIC')

        if photos.count():
            image = photos.order_by('?').first()
            pic_path = image.image.url
            image_title = image.title

        else:
            pic_path = 'http://via.placeholder.com/250x250'
            image_title = 'Placeholder'

        context['pic_path'] = pic_path
        context['image_title'] = image_title
        context['message'] = 'Hello World'

        return context
