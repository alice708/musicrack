from django.contrib import admin

from .models import Artist,Album,Song


class ArtistAdmin(admin.ModelAdmin):
    fields = ["name", "genre", "id"]
    list_display = ["name", "genre"]

admin.site.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
    fields = ["name", "year_released", "id", "artist"]
    list_display = ["name", "year_released", "artist"]
admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    fields = ["name", "length", "id", "album"]
    list_display = ["name", "length", "album"]
admin.site.register(Song, SongAdmin)

