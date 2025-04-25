import argparse
from django.core.management.base import BaseCommand, CommandError
from data.models import Artist,Album,Song

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--id", required=True, type=str)
        parser.add_argument("--name", required=True, type=str)
        parser.add_argument("--length", required=True, type=str)
        parser.add_argument("--album", required=True, type=str)


    def handle(self, *args, **options):
        song = Song.create(id = options["id"], name = options["name"], length = options["length"], album = options["album"])
        song.save()