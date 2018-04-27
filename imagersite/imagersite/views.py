from django.shortcuts import render
from imager_images.models import Photo


def home_view(request):
    """View is for homepage."""
    photos = Photo.objects.all()
    photos = photos.filter(published='PUBLIC')

    context = {
        'message': 'Hellow World',
        'photos': photos,
    }

    return render(request, 'generic/home.html', context)
