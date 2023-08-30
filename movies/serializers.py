from rest_framework import serializers
from movies.models import Genre, Movie


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class MoviesSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)
    # genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'genres',
                  'release_date', 'vote_average', 'vote_count']

    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)

        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)

        return movie

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genres')
        instance = super().update(instance, validated_data)

        instance.genres.clear()

        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            instance.genres.add(genre)

        return instance
