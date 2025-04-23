from django.db import models

class Song(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    # Make this a custom field of 2 integers
    # Or make this 2 fields, mins/secs and display it as one?
    length = models.CharField(max_length=200)

    @classmethod
    def create(cls, id, name, length):
        song = cls(id=id, name=name, length=length)
        return song

class Album(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    year_released = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class Artist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)