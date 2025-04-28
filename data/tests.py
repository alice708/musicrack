from django.test import TestCase
from .management.commands.uploadfile import Command as UploadFile

class UploadFileTests(TestCase):
    
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
