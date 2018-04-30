"""Image Urls."""

from django.urls import path
from .views import image_view, image_photo_view, library_view, photo_detail_view, photo_view


urlpatterns = [
    path('', image_view, name='image'),
    path('photos', photo_view, name='photo'),
    path('photos/<int:id>', photo_detail_view, name='photo_detail'),
    path('library', library_view, name='library')
]
