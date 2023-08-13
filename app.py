from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


def read_movies_data():
    with open("Merged_Movies_data.json", "r") as file:
        data = json.load(file)
        return data


@app.get("/", response_model=str)
def get_homepage():
    return "Hello !"


@app.get("/movies/", response_model=list)
def get_all_movies():
    return read_movies_data()


@app.get("/movies/name/{movie_name}", response_model=list)
def get_movies_by_name(movie_name: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie
        for movie in all_movies
        if movie_name.lower() in movie["movieName"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movie not found for the specific name"
        )
    return filtererd_movies


@app.get("/movies/year/{movie_year}", response_model=list)
def get_movies_by_year(movie_year: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie for movie in all_movies if movie_year.lower() in movie["movieYear"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movie not found for the specific year"
        )
    return filtererd_movies


@app.get("/movies/rating/{movie_rating}", response_model=list)
def get_movies_by_rating(movie_rating: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie for movie in all_movies if  movie_rating in movie["movieRating"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movies not found for the specific genre"
        )
    return filtererd_movies


@app.get("/movies/genre/{movie_genre}", response_model=list)
def get_movies_by_genre(movie_genre: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie for movie in all_movies if movie_genre.lower() in movie["movieGenre"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movies not found for the specific genre"
        )
    return filtererd_movies


@app.get("/movies/director/{movie_director}", response_model=list)
def get_movies_by_director(movie_director: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie for movie in all_movies if movie_director.lower() in movie["movieDirector"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movies not found for the specific director"
        )
    return filtererd_movies


@app.get("/movies/cast/{movie_cast}", response_model=list)
def get_movies_by_cast(movie_cast: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie for movie in all_movies if movie_cast.lower() in movie["movieStars"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movies not found for the specific cast"
        )
    return filtererd_movies

@app.get("/movies/certificate/{movie_certi}", response_model=list)
def get_movies_by_certi(movie_certi: str):
    all_movies = get_all_movies()
    filtererd_movies = [
        movie for movie in all_movies if movie_certi.lower() in movie["movieCertificate"].casefold()
    ]
    if not filtererd_movies:
        raise HTTPException(
            status_code=404, detail="Movies not found for the specific cast"
        )
    return filtererd_movies