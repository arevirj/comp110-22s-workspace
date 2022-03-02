"""Testing functions from dictionary.py."""

__author__: str = "730488173"

from dictionary import invert, count, favorite_color
import pytest


# Tests for the invert function

def test_invert_many() -> None:
    """Use case: that the invert function switches the key-value pairs of whatever funciton is inputted with several pairs."""
    x: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(x) == {'b': 'a', 'd': 'c'}


def test_invert_single() -> None:
    """Use case: tests that the invert function switches the key-value pairs of the parameter dictionary when only one pair exists."""
    x: dict[str, str] = {'a': 'b'}
    assert invert(x) == {'b': 'a'}


def test_invert_error() -> None:
    """Edge case: tests that when the parameter dicionary has repeated values, that in the invert function, A KeyError will occur."""
    with pytest.raises(KeyError):
        x = {'a': 'b', 'c': 'b'}
        invert(x)


# Tests for the count function

def test_count_many() -> None:
    """Use case: tests that when given a list with many items, the count function will return a dicitonary with each item and their respective instances as a key value pair."""
    x: list[str] = ['yellow', 'green', 'blue', 'blue']
    assert count(x) == {'yellow': 1, 'green': 1, 'blue': 2}


def test_count_single() -> None:
    """Use case: tests that when given a list with one item, the count funciton will return a dictionary with one key-value pair."""
    x: list[str] = ['blue']
    assert count(x) == {'blue': 1}


def test_count_empty() -> None:
    """Edge case: tests that when given an empty list, the count function will return an empty dictionary."""
    x: list[str] = list()
    assert count(x) == {}


# Tests for the favorite color function

def test_favorite_color_many() -> None:
    """Use case: tests that when given a dictionary that has multiple values, and one value occurs the most, that value is returned as a string."""
    x: dict[str, str] = {'m': 'yellow', 'e': 'blue', 'k': 'blue'}
    assert favorite_color(x) == 'blue'


def test_favorite_color_even() -> None:
    """Use case: tests that when given a dictionary that has multiple values, but all occur in even intervals, that the first ordered value is returned as a string."""
    x: dict[str, str] = {'m': 'yellow', 'k': 'blue'}
    assert favorite_color(x) == 'yellow'


def test_favorite_color_single() -> None:
    """Edge case: tests that when given dictionary with a single pair, that the value will be returned."""
    x: dict[str, str] = {'b': 'blue'}
    assert favorite_color(x) == 'blue'