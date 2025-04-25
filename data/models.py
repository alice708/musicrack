from django.db import models

class Artist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Album(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    year_released = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    # Make this a custom field of 2 integers
    # Or make this 2 fields, mins/secs and display it as one?
    length = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    @classmethod
    def create(cls, id, name, length, album):
        song = cls(id=id, name=name, length=length, album=album)
        return song
