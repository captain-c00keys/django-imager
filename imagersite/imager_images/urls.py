"""Image Urls."""

from django.urls import path
from .views import image_view, image_photo_view, image_one_photo


urlpatterns = [
    path('', image_view, name='image'),
    path('photos', image_photo_view, name='image_photo'),
    path('photos/<int:photo_id>', image_photo_view, name='image_photo'),
    path('library', library_view, name='library')
]
