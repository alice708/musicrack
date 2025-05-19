from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from data.models import Artist,Album,Song
import csv
from  django.utils.dateparse import parse_duration, parse_date


class Command(BaseCommand):
    help = "Uploads music data from a file. See README for usage"

    def add_arguments(self, parser):
        parser.add_argument("--file", required=True, type=str)

    def is_artist_row(self, row):
        # Row[2] is either the artist`s genre, the album`s year release or a song`s length
        # the latter two contain digits so a row[2] that contians no digits should mean that
        # the row represents an artist
        return not any(char.isdigit() for char in row[2])   
    
    def is_album_row(self, row):
        # Assume year released is exactly 4 digits
        return all(char.isdigit() for char in row[2]) and len(row[2]) == 4
    

    def handle(self, *args, **options):

        # Save tuples of fields for each object we will create
        # We can't create the objects yet due to them referencing eachother
        artist_list = []
        album_list = []
        song_list = []

        with open(options["file"], newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter='|')

            current_artist_id = None
            current_album_id = None

            for row in filereader:
                if self.is_artist_row(row):
                    artist_list.append((row[0], row[1], row[2]))
                    current_artist_id = row[0]
                    # Set the current album to none since the previous album belonged to a
                    # different artist and the next row should contain a new album (or another artist)
                    current_album_id = None
                # Can only create an Album if it belongs to an Artist
                elif current_artist_id is not None and self.is_album_row(row):
                    # Put 1st Jan as defaults, since we can't just specify year
                    date = datetime(int(row[2]), 1, 1)
                    album_list.append((row[0], row[1],date, current_artist_id))
                    current_album_id = row[0]
                # Can only create a Song if it belongs to an Album
                elif current_album_id is not None:
                    song_list.append((row[0], row[1], parse_duration(row[2]), current_album_id))
                else:
                    error = "Song file not in correct format, see README for correct format"
                    self.stderr.write(error)
                    raise Exception(error)
                
        # Only save the objects once we have succesfully parsed the whole file, to 
        # make sure uploading the file is atomic.

        artist_object_list = []
        for artist in artist_list:
            artist_object_list.append(Artist.create(id=artist[0], name=artist[1], genre=artist[2]))
        Artist.objects.bulk_create(artist_object_list)

        album_object_list = []
        for album in album_list:
            album_object_list.append(Album.create(id=album[0], name=album[1], year_released=album[2], artist=album[3]))
        Album.objects.bulk_create(album_object_list)

        song_object_list = []
        for song in song_list:
            song_object_list.append(Song.create(id=song[0], name=song[1], length=song[2], album=song[3]))
        Song.objects.bulk_create(song_object_list)

        self.stdout.write("Succesfully uploaded song file data")
                