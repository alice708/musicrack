from django.contrib import admin

from .models import Artist,Album,Song


class ArtistAdmin(admin.ModelAdmin):
    fields = ["name", "genre", "id"]
    list_display = ["name", "genre"]
    search_fields = ["name", "genre"]

admin.site.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
    fields = ["name", "year_released", "id", "artist"]
    list_display = ["name", "year_released", "artist"]
    search_fields = ["name", "year_released", "artist__name"]
admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    fields = ["name", "length", "id", "album"]
    list_display = ["name", "length", "album"]
    search_fields = ["name", "length", "album__name"]
admin.site.register(Song, SongAdmin)

