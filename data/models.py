from django.db import models

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    song_length = models.IntegerField()

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    year_released = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)