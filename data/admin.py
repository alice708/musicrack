from django.contrib import admin

from .models import Artist,Album,Song

class SongAdmin(admin.ModelAdmin):
    fields = ["name", "length", "id", "album"]
    list_display = ["name", "length", "album"]
    search_fields = ["name", "length", "album__name"]
admin.site.register(Song, SongAdmin)

class SongInLine(admin.TabularInline):
    model = Song

class AlbumAdmin(admin.ModelAdmin):
    fields = ["name", "year_released", "id", "artist"]
    list_display = ["name", "year", "artist"]
    search_fields = ["name", "year_released", "artist__name"]
    inlines = [SongInLine]
admin.site.register(Album, AlbumAdmin)

class AlbumInLine(admin.TabularInline):
    model = Album

class ArtistAdmin(admin.ModelAdmin):
    fields = ["name", "genre", "id"]
    list_display = ["name", "genre"]
    search_fields = ["name", "genre"]
    inlines = [AlbumInLine]

admin.site.register(Artist, ArtistAdmin)
