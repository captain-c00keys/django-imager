"""Image Urls."""

from django.urls import path
from .views import image_view, image_photo_view, library_view
from .views import image_album_view, image_detail_album_view
from .views import image_detail_photo_view


urlpatterns = [
    path('', image_view, name='image'),
    path('photos', image_photo_view, name='image_photo'),
    path('albums', image_album_view, name='image_album'),
    path(
        'photos/<int:photo_id>',
        image_detail_photo_view,
        name='image_photo_detail'),
    path(
        'albums/<int:photo_id>',
        image_detail_album_view,
        name='image_album_detail'),
    path('library', library_view, name='library'),
]
