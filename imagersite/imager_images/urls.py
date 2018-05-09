"""Image Urls."""
from django.urls import path
from .views import library_view, PhotoView, AlbumView, \
     AlbumDetail, PhotoDetail


urlpatterns = [
    path('library/', library_view, name='library'),
    path('albums/', AlbumView.as_view(), name='albums'),
    path('photos/', PhotoView.as_view(), name='photos'),
    path('albums/<int:id>', AlbumDetail.as_view(), name='album_detail'),
    path('photos/<int:id>', PhotoDetail.as_view(), name='photo_detail'),
]
