import argparse
from django.core.management.base import BaseCommand, CommandError
from data.models import Artist,Album,Song

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--file", required=True, type=str)

    def is_artist_row(self, field):
        # Assume artist contians no digits.
        # Not true, but is true for the song.txt file so do this for now to prototype the code
        return not any(char.isdigit() for char in field)   

    def handle(self, *args, **options):
        import csv
        with open(options["file"], newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter='|')

            last_row_was_artist = False
            last_id = ""

            for row in filereader:
                print(', '.join(row))
                if self.is_artist_row(row[2]):
                    Artist.create(id=row[0], name=row[1], genre=row[2]).save()
                    last_row_was_artist = True
                    last_id = row[0]
                elif last_row_was_artist:
                    Album.create(id=row[0], name=row[1], year_released=row[2], artist=last_id).save()
                    last_id = row[0]
                    last_row_was_artist = False
                else:
                    Song.create(id=row[0], name=row[1], length=row[2], album=last_id).save()
                




