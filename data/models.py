from django.db import models

class Artist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
       return self.name

    @classmethod
    def create(cls, id, name, genre):
        artist = cls(id=id, name=name, genre=genre)
        return artist

class Album(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    year_released = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

    @classmethod
    def create(cls, id, name, year_released, artist):
        album = cls(id=id, name=name, year_released=year_released, artist=Artist.objects.get(id=artist))
        return album

class Song(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

    @classmethod
    def create(cls, id, name, length, album):
        song = cls(id=id, name=name, length=length, album=Album.objects.get(id=album))
        return song
