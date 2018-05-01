"""Admin site."""
from django.contrib import admin
from .models import Album, Photo

admin.site.register((Album, Photo))
