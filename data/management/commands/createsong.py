import argparse
from django.core.management.base import BaseCommand, CommandError
from data.models import Artist,Album,Song

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--id", required=True, type=str)
        parser.add_argument("--name", required=True, type=str)
        parser.add_argument("--length", required=True, type=int)


    def handle(self, *args, **options):
        self.stdout.write(
                self.style.SUCCESS('You entered "%s"' % options["name"])
            )
        self.stdout.write(
                self.style.SUCCESS('You entered "%s"' % options["length"])
            )
        song = Song.create(id = options["id"], name = options["name"], length = options["length"])
        song.save()