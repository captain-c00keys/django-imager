"""Home view."""

from django.shortcuts import render
from imager_images.models import Photo
from random import choice


def home_view(request):
    """View is for homepage."""
    photos = Photo.objects.all()
    photos = photos.filter(published='PUBLIC')
    # import pdb; pdb.set_trace()
    if len(photos) > 0:
        rand_pick = choice(photos)
        pic_path = rand_pick.image.url

# work on the below else. See where it connects to

    else:
        pic_path = None

    context = {
        'message': 'Hellow World',
        'photos': photos,
        'pic_path': pic_path
    }

    return render(request, 'generic/home.html', context)
