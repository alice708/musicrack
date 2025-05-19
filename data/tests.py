from io import StringIO
from django.test import TestCase
from .management.commands.uploadfile import Command as UploadFile
from django.core.management import call_command
import csv
from .models import Artist, Album, Song

class UploadFileValidatorTests(TestCase):
    
    def test_is_artist_row_correct(self):
        artist_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Coldplay", "rock"]
        self.assertIs(UploadFile.is_artist_row(UploadFile, artist_row), True)

    def test_is_artist_row_contains_digit(self):
        artist_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Coldplay", "r0ck"]
        self.assertIs(UploadFile.is_artist_row(UploadFile, artist_row), False)
    
    def test_is_artist_row_empty_genre(self):
        artist_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Coldplay", ""]
        self.assertIs(UploadFile.is_artist_row(UploadFile, artist_row), True)

    def test_is_album_row_correct(self):
        album_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Skin", "2016"]
        self.assertIs(UploadFile.is_album_row(UploadFile, album_row), True)

    def test_is_album_row_contains_letter(self):
        album_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Skin", "Twenty Sixteen"]
        self.assertIs(UploadFile.is_album_row(UploadFile, album_row), False)
    
    def test_is_album_row_not_4_digits(self):
        album_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Skin", "16"]
        self.assertIs(UploadFile.is_album_row(UploadFile, album_row), False)

    def test_is_album_row_empty(self):
        album_row = ["4gzpq5DPGxSnKTe4SA8HAU", "Skin", ""]
        self.assertIs(UploadFile.is_album_row(UploadFile, album_row), False)

class UploadFileHandleTests(TestCase):
    def call_command(self, *args, **options):
        out = StringIO()
        call_command(
            "uploadfile",
            *args,
            stdout=out,
            stderr=StringIO(),
            **options,
        )
        return out.getvalue()
    
    # Test a simple song file and check the song album and artist are correctly 
    # uploaded to the database   
    def test_uploading_correct_song_file(self):
        artist = ['4gzpq5DPGxSnKTe4SA8HAU', 'Coldplay', 'rock']
        album = ['0RHX9XECH8IVI3LNgWDpmQ', 'A Rush of Blood to the Head', '2002']
        song = ['0u35Dpz37TY2M2j20RUdMf', 'Politik', '5:18']

        with open('test.txt', 'w') as csvfile:
            songwriter = csv.writer(csvfile, delimiter='|')
            songwriter.writerow(artist)
            songwriter.writerow(album)
            songwriter.writerow(song)

        out = self.call_command("--file", "test.txt")
        self.assertEqual(out, "Succesfully uploaded song file data\n")

        result_artist = Artist.objects.get(id=artist[0])
        self.assertEqual(result_artist.name, artist[1])
        self.assertEqual(result_artist.genre, artist[2])

        result_album = Album.objects.get(id=album[0])
        self.assertEqual(result_album.name, album[1])
        self.assertEqual(str(result_album.year_released), "2002-01-01") # Year stored as a date with 1st Jan

        result_song = Song.objects.get(id=song[0])
        self.assertEqual(result_song.name, song[1])
        self.assertEqual(result_song.length.seconds, 5*60+18) # Length stored as a datetime timedelta

        import os
        os.remove("test.txt")


    # Test a more complicated song file with multiple songs, albums and artists.
    # Only do a few checks, e.g. that a second album can be added for an artist. 
    def test_uploading_correct_complicated_song_file(self):
        x = """4gzpq5DPGxSnKTe4SA8HAU|Coldplay|rock|
0RHX9XECH8IVI3LNgWDpmQ|A Rush of Blood to the Head|2002|
0u35Dpz37TY2M2j20RUdMf|Politik|5:18|
2nvC4i2aMo4CzRjRflysah|In My Place|3:36|
aaaaaaECH8IVI3LNgWDpmQ|Second Coldplay Album|2002|
4hf0hL4kWyjWztZzVsM39V|God Put a Smile upon Your Face|4:57|
34EP7KEpOjXcM2TCat1ISk|Wu-Tang Clan|hip-hop|
3tQd5mwBtVyxCoEo4htGAV|Enter The Wu-Tang (36 Chambers)|1993|
1v5cgIyffYtfEx0swttdoE|Bring Da Ruckus|4:11|
7IwURvEfVcdxUCjLKUu6sv|Shame On a N***a|2:57|
4LaiF2h7gsybmURceGYLqh|Clan In Da Front|4:33|
6nxWCVXbOlEVRexSbLsTer|Flume|dance|
1sxqYNzozsrgu0Vh6jQ6Lr|Skin|2016|
79uaE0SyKAz90xMWHLDgjL|Helix|3:30|
476j7IDRIDRvv1Xu71EVc8|Never Be Like You|3:53|
7zD7iZPRbfB0NSPuFNpkRH|Lose It|3:45|"""

        with open('test.txt', 'w') as f:
            f.writelines(x)

        out = self.call_command("--file", "test.txt")
        self.assertEqual(out, "Succesfully uploaded song file data\n")

        result_artist = Artist.objects.get(id='4gzpq5DPGxSnKTe4SA8HAU')
        self.assertEqual(result_artist.name, 'Coldplay')

        result_album1 = Album.objects.get(id='0RHX9XECH8IVI3LNgWDpmQ')
        self.assertEqual(result_album1.name, 'A Rush of Blood to the Head')

        result_album2 = Album.objects.get(id='aaaaaaECH8IVI3LNgWDpmQ')
        self.assertEqual(result_album2.name, 'Second Coldplay Album')

        import os
        os.remove("test.txt")



    def test_uploading_incorrect_song_file(self):
        # Incorrect file since the first line is not an artist
        x = """4gzpq5DPGxSnKTe4SA8HAU|Coldplay|1999|"""
        with open('test.txt', 'w') as f:
            f.writelines(x)
        
        with self.assertRaises(Exception):
            self.call_command("--file", "test.txt")

        import os
        os.remove("test.txt")

        


        





        

