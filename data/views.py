from django.shortcuts import render

from .models import Album, Song

def song(request, id):
    song = Song.objects.get(pk=id)
    #album = Album.objects.get(pk=song.album).name
    context = {"name": song.name,"length": song.length,"id": song.id, "album": song.album.name}
    return render(request, "data/song.html", context) 