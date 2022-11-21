import typing
import datetime
import requests
import urllib.parse


MOVIE_ADDRESS = "https://api.themoviedb.org/3/search/movie?"


def movie_search(movie: str, movieDBKey: str) -> typing.Union[str, int]:
    movieAddressSearch = f"""{MOVIE_ADDRESS}{urllib.parse.urlencode({"api_key": movieDBKey})}&{urllib.parse.urlencode({"query": movie})}"""
    movieSearchJsonData = requests.get(movieAddressSearch).json()
    title = movieSearchJsonData["results"][0]["title"]
    year = datetime.datetime.strptime(
        movieSearchJsonData["results"][0]["release_date"], "%Y-%m-%d"
    ).year
    return title, year
