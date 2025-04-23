from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField()

    @classmethod
    def create(cls, name, length):
        song = cls(name=name, length=length)
        # do something with the book
        return song

class Album(models.Model):
    name = models.CharField(max_length=200)
    year_released = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)