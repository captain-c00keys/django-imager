"""Image Urls."""
from django.urls import path
from .views import LibraryView, PhotoView, AlbumView, \
     AlbumDetail, PhotoDetail, AddPhoto


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('albums/', AlbumView.as_view(), name='albums'),
    path('photos/', PhotoView.as_view(), name='photos'),
    path('albums/<int:id>', AlbumDetail.as_view(), name='album_detail'),
    path('photos/<int:id>', PhotoDetail.as_view(), name='photo_detail'),
    path('photos/add', AddPhoto.as_view(), name='add_photo')
]
