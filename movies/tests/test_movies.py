from rest_framework.test import APIClient
from rest_framework import status
import pytest
from model_bakery import baker
from movies.models import Genre, Movie


@pytest.mark.django_db
class TestGetMovies:
    def test_if_movie_not_exists_404(self):
        api_client = APIClient()
        response = api_client.get('/cine/movies/-10/')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_create_movie_with_incomplete_data_returns_400(self):
        api_client = APIClient()
        response = api_client.post(
            '/cine/movies/', {'title': 'a', 'description': 'b'}, format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_create_movie_with_valid_data_returns_201(self):
        api_client = APIClient()

        response = api_client.post('/cine/movies/', {
            "title": "Test Movie",
            "description": "This is a test movie description.",
            "genres": [],
            "release_date": "2000-09-09",
            "vote_average": "3.0",
            "vote_count": 3,
        }, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_non_existant_movie_returns_404(self):
        api_client = APIClient()
        response = api_client.delete('cine/movies/0/')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_movie_returns_204(self):
        api_client = APIClient()
        movie = baker.make(Movie)
        response = api_client.delete(f'/cine/movies/{movie.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_get_movie_that_exists_returns_200(self):
        api_client = APIClient()
        movie = baker.make(Movie)
        response = api_client.get(f'/cine/movies/{movie.id}/')

        assert response.status_code == status.HTTP_200_OK

    
    def test_update_movie(self):
        api_client = APIClient()
        movie = baker.make(Movie)

        response = api_client.put(f'/cine/movies/{movie.id}/',{
            "title": "Test Movie",
            "description": "This is a test movie description.",
            "genres": [],
            "release_date": "2000-09-09",
            "vote_average": "3.0",
            "vote_count": 3,
        }, format='json')

        assert response.status_code == status.HTTP_200_OK