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

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
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
                #     movie.save()
                # movie.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))


# def clean_data(file):
#     with open(file, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in list(reader)[:5]:  # To just show the first 5 rows
#             json_genres = row['genres'].replace("'", "\"")
#             genres = json.loads(json_genres)
#             for genre in genres:
#                 print(genre['name'])


# def new_clean_data(file):
#     with open(file, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             genres_data = eval(row['genres'])
#             genres = [Genre.objects.get_or_create(name=genre['name'])[0] for genre in genres_data]

#             movie = Movies.objects.create(
#                 title=row['title'],
#                 description=row['description'],
#                 release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
#                 vote_average=Decimal(row['vote_average']),
#                 vote_count=int(row['vote_count'])
#             )
#             movie.genres.set(genres)

#     print("Data imported successfully.")


# if __name__ == '__main__':
#     new_clean_data('data\movies_metadata.csv')
