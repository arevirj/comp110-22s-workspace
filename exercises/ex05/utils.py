"""Functions carrying out different objectives."""

__author__: str = "730488173"


def only_evens(x: list[int]) -> list[int]:
    """Function that returns a list of only the even integers of a list given in the parameter."""
    # Creating empty list to be returned at end.
    even_list: list[int] = list()
    # for_in_ loop in order to append the even integers of given list.
    for item in x:
        if item % 2 == 0:
            even_list.append(item)
    return even_list


def sub(x: list[int], n: int, r: int) -> list[int]:
    """Returns a subset of an entered between two indexes."""
    # creating empty list, counting variables, and assigning index parameters variables so that they might be changed for later conditions.
    subset: list[int] = list()
    i: int = 0
    start: int = n
    end: int = r
    # Ensuring an empty list would be returned if either length of list is 0,the start > len of list,
    # or if end of list is <= 0.
    if len(x) == 0:
        return subset
    elif n > len(x):
        return subset
    elif r <= 0:
        return subset
    # If the start index is a negative number, the list will start from beginning.
    if n < 0:
        start = 0 
    # if end index is bigger than list length, the list will end with the end of the list.
    if r > len(x):
        end = len(x)
    i = start
    # loop to create the returned list
    while i < end:
        subset.append(x[i])
        i += 1
    return subset


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Returns a combination of two lists in the order they were given."""
    # create empty list to be returned
    biglist: list[int] = list()
    # for_in_ loop to append the first list first.
    for item in first_list:
        biglist.append(item)
    # for_in_ loop to append the second list second.
    for item in second_list:
        biglist.append(item)
    return biglist