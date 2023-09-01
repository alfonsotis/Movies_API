import csv
from decimal import Decimal
from pathlib import Path
import json
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre


class Command(BaseCommand):
    help = 'Import movies from CSV file'

    def handle(self, *args, **kwargs):

        current_dir = os.path.dirname(__file__)
        file_path = Path(current_dir, 'movies_metadata.csv')
        not_defined_genre, _ = Genre.objects.get_or_create(name='Not defined')
        count = 0
        limit = 1500

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if count >= limit:
                    break
                genres_data = eval(row['genres'])
                genres = [Genre.objects.get_or_create(name=genre['name'])[
                    0] for genre in genres_data]

                if not genres:
                    genres.append(not_defined_genre)

                try:
                    release_date = datetime.strptime(
                        row['release_date'], '%Y-%m-%d').date()
                except ValueError:
                    release_date = '0001-01-01'

                movie = Movie.objects.create(
                    title=row['title'],
                    description=row['overview'],
                    release_date=release_date,
                    vote_average=Decimal(row['vote_average']),
                    vote_count=int(row['vote_count'])
                )

                movie.genres.set(genres)
                count += 1


        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))

