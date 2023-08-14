# Movie Data Scraping and API

This project involves scraping movie data from IMDb website and providing an API to access and query the collected movie information.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Description

The project consists of two main parts:

1. **Movie Data Scraping:** The `scrap` function in the script `scrap.py` is responsible for scraping movie data from IMDb website for the specified years. The data includes movie name, year, certificate, rating, runtime, genre, director, stars, and link.

2. **FastAPI Web API:** The `main.py` script uses the FastAPI framework to create a web API that provides endpoints to retrieve and query the scraped movie data. The API offers various endpoints to filter and search for movies based on different criteria such as name, year, rating, genre, director, cast, and certificate.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Adarshh9/Movie_API.git
   ```

2. Install the required Python packages:

   ```bash
   pip install requests_html fastapi uvicorn
   ```

## Usage

1. Run the movie data scraping script:

   ```bash
   python scrap.py
   ```

   This script scrapes movie data from IMDb for specified years and saves it to a JSON file named `Merged_Movies_data.json`.

2. Start the FastAPI web API:

   ```bash
   uvicorn app:app --reload --host 0.0.0.0
   ```

   The API will be accessible at http://localhost:8000/docs.

## API Endpoints

- **GET /movies/name/{movie_name}**: Get a list of movies matching the specified name.

- **GET /movies/year/{movie_year}**: Get a list of movies released in the specified year.

- **GET /movies/rating/{movie_rating}**: Get a list of movies with the specified rating.

- **GET /movies/genre/{movie_genre}**: Get a list of movies belonging to the specified genre.

- **GET /movies/director/{movie_director}**: Get a list of movies directed by the specified director.

- **GET /movies/cast/{movie_cast}**: Get a list of movies featuring the specified cast.

- **GET /movies/certificate/{movie_certi}**: Get a list of movies with the specified certificate.

- **GET /movies/**: Get a list of all movies.

## Contributing

Contributions to this project are welcome. If you find any issues or want to enhance the project, feel free to create a pull request.

---

*Note: This README provides a basic overview of the project. You may want to customize and expand it to provide more detailed information about the project, installation steps, usage examples, and other relevant details.*
