# Movie API Documentation

This API allows you to access and manage a list of movies. Below are the available endpoints and their usage:

## Movies List GET Endpoint

- **Endpoint**: `http://127.0.0.1:8000/cine/movies/`
- **Method**: GET
- **Description**: Get a list of all movies.

## GET Movie by ID Endpoint

- **Endpoint**: `http://127.0.0.1:8000/cine/movies/<int:id>/`
- **Method**: GET
- **Description**: Get a specific movie by its ID.

## Movies POST Endpoint

- **Endpoint**: `http://127.0.0.1:8000/cine/movies/`
- **Method**: POST
- **Description**: Create a new movie.
- **Format Example**:
  ```json
  {
      "title": "Z",
      "description": "Z",
      "genres": [{"name": "genre"}, {"name": "genre2"}],
      "release_date": "1995-11-16",
      "vote_average": 5,
      "vote_count": 5
  }

## Movies DELETE Endpoint

- **Endpoint**: `http://127.0.0.1:8000/cine/movies/<int:id>/`
- **Method**: DELETE
- **Description**: Delete a movie by its ID.

## Movies Update PUT Endpoint

- **Endpoint**: `http://127.0.0.1:8000/cine/movies/<int:id>/`
- **Method**: PUT
- **Description**: Update a movie by its ID. Use the same format as the POST endpoint.

## Search Movies

- **Endpoint**: `http://127.0.0.1:8000/cine/movies/?search=<Term>`
- **Method**: GET
- **Description**: Search for movies using a search term.

## Filtering Movies

To filter movies, use the following URL format:

- **URL**: `http://127.0.0.1:8000/cine/movies/?genres__name=<Term>&vote_average=<Term>&release_date__gt=<Term>&release_date__lt=<Term>`

Replace `<Term>` with the value you want to filter by. You can also remove `<Term>` from the URL, or remove fields from the URL that you don't want to filter. For example:

- Filter by genre:
  - `http://127.0.0.1:8000/cine/movies/?genres__name=Comedy`
