import sys
import os
import pytest

sys.path.insert(0, "/Users/kingamazur/PycharmProjects/dareit-waw-cinema-assistant/") 

from Movie import Movie

@pytest.fixture
def movie():
    return Movie(
        rating = 8.8,
        time="19:00", 
        cinema="Cinema City", 
        title="Inception", 
        base_url="https://example.com/inception", 
        director="Christopher Nolan", 
        year=2010
    )

def test_to_dictionary(movie):
    expected_dict = {
        'rating': 8.8,
        'time': "19:00",
        'cinema': "Cinema City",
        'title': "Inception",
        'link': "https://example.com/inception",
        'director': "Christopher Nolan",
        'year': 2010}
    assert movie.to_dictionary() == expected_dict

def test_set_rating(movie):
    movie.set_rating()
    assert movie.rating == 8.8