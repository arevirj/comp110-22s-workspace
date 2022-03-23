"""Testing functions from utils."""


__author__: str = "730488173"

from utils import only_evens, sub, concat

# Tests of the only_evens function.


def test_only_evens_empty() -> None:
    """Testing if only_evens will return an empty list when given an empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_all_odd() -> None:
    """Testing if only_evens will return an empty list when only odd numbers are given."""
    x: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(x) == []


def test_only_evens_main() -> None:
    """Testing if only_evens will return all even numbers from a list with both even and odd integers."""
    x: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(x) == [2, 4, 6, 8]


# Tests of the sub function.


def test_sub_empty() -> None:
    """Testing if the sub function will return an empty list when the parameter list is empty."""
    x: list[int] = []
    start: int = 1
    end: int = 4
    assert sub(x, start, end) == []


def test_sub_start_negative() -> None:
    """Testing if sub funciton will start from first index if it is negative, regardless of start parameter."""
    x: list[int] = [1, 2, 3, -4, 5, 6, 7]
    start: int = -3
    end: int = 6
    assert sub(x, start, end) == [1, 2, 3, -4, 5, 6]


def test_sub_end_greater() -> None:
    """Testing if when the end index of sub function is greater than the length of list, it will end with the end of the list."""
    x: list[int] = [1, 2, 3, 9, 4]
    start: int = 1
    end: int = 9
    assert sub(x, start, end) == [2, 3, 9, 4]


def test_sub_start_greater() -> None:
    """Testing if when the start parameter is greater than length of the list, the sub function will return an empty list."""
    x: list[int] = [1, 2, 3]
    start: int = 4
    end: int = 5
    assert sub(x, start, end) == []


def test_sub_end_small() -> None:
    """Testing if when end parameter of sub function is <= 0, the function will return empty list."""
    x: list[int] = [1, 2, 3]
    start: int = 1
    end: int = 0
    assert sub(x, start, end) == []


def test_sub_main() -> None:
    """Testing if the sub function works when given normal parameters."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 1
    end: int = 4
    assert sub(x, start, end) == [2, 3, 4]

# Tests of the concat function.


def test_concat_empty_1() -> None:
    """Testing if when the concat function is given a single empty list, it will still return the other list in order."""
    first: list[int] = []
    second: list[int] = [4, 5, 6]
    assert concat(first, second) == [4, 5, 6]


def test_concat_empty_2() -> None:
    """Testing if when the concat function is given two empty lists, it will return an empty list."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_main() -> None:
    """Testing if the concat function returns the first and the second list combined in order."""
    first: list[int] = [1, 2, 3, 4, 5]
    second: list[int] = [11, 22, 33, 44, 55]
    assert concat(first, second) == [1, 2, 3, 4, 5, 11, 22, 33, 44, 55]