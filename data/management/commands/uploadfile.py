from django.core.management.base import BaseCommand, CommandError
from data.models import Artist,Album,Song
import csv

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--file", required=True, type=str)

    def is_artist_row(self, row):
        # Row[2] is either the artists genre, the albums year release or the songs length
        # the latter two contain digits so a row[2] that contians no digits should mean that
        # the row represents an artsit
        # The genre not containing digits isn't neccaserily true, but is true for the
        # song.txt file so do this for now to prototype the code
        return not any(char.isdigit() for char in row[2])   
    
    def is_album_row(self, row):
        # Assume year released is exactly 4 digits
        return all(char.isdigit() for char in row[2]) and len(row[2]) == 4

    def handle(self, *args, **options):
        with open(options["file"], newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter='|')

            current_artist_id = None
            current_album_id = None

            for row in filereader:
                # If artist row then set the current album to none since the previous
                # album was a different artist and the next row should contain an album 
                if self.is_artist_row(row):
                    Artist.create(id=row[0], name=row[1], genre=row[2]).save()
                    current_artist_id = row[0]
                    current_album_id = None
                # The check for an artist id is only to check that the first row was an artist
                elif current_artist_id != None and self.is_album_row(row):
                    Album.create(id=row[0], name=row[1], year_released=row[2], artist=current_artist_id).save()
                    current_album_id = row[0]
                elif current_album_id != None:
                    Song.create(id=row[0], name=row[1], length=row[2], album=current_album_id).save()
                else:
                    error = "Song file not in correct format, see README for correct format"
                    self.stderr.write(error)
                    raise Exception(error)
                
        self.stdout.write("Succesfully uploaded song file")
                