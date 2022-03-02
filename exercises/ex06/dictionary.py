"""Making dictionary funcitons."""

__author__: str = "730488173"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Funciton that when given key-value pairs, inverts them so that the value becomes the key and vice versa."""
    # Create new dictionary to place the inverted key-values in
    y: dict[str, str] = {}
    # Create a list that can be checked to ensure no keys are repeated
    vals: list[str] = list()
    # Counts how many times each value appears in the new dictionary.
    instances: int = 0 
    # For_in loop that creates the new dictionary and adds values to the vals list
    for key in x:
        y[x[key]] = key
        vals.append(x[key])  
        i: int = 0
        # While loop that checks the instances of each unique key in dicitonary
        while i < len(vals):
            if vals[i] == x[key]:
                instances += 1
            i += 1
        i = 0
    # If statement to raise a KeyError if a key was used more than once.
    if instances > len(vals):
        raise KeyError("A key was used more than once.")
    else:
        return y


def count(vals: list[str]) -> dict[str, int]:
    """Function that when given a list of strings, returns a dictionary of key value pairs witht they keys being the strings in the parameter list, and the values being the number of times they appear in the list."""
    # Create empty dictionary that will be returned.
    instances: dict[str, int] = dict()
    # For_in loop that will create the new dictionary
    for item in vals:
        # If else statement that will create a key in the new dicitonary starting at value 1, and then add to it.
        if item in instances:
            instances[item] += 1
        else:
            instances[item] = 1
    return instances


def favorite_color(favs: dict[str, str]) -> str:
    """Funciton that when given a dictionary of key-value pairs, returns the value that appeared the most as a string."""
    # Create empty list for values to be stored
    colors: list[str] = list()
    # For_in loop to add the values from the dictionary to the empty list.
    for name in favs:
        colors.append(favs[name])
    # count function is used to create a variable of a dictionary with the values and their instances as key-value pairs.
    color_amount: dict[str, int] = count(colors)
    # variable to keep track of biggest amount of instances
    x: int = 0 
    # string variable to be returned at the end of the function
    win: str = ""
    # for_ in loop to evaluate which color has the most instances.
    for item in color_amount:
        if color_amount[item] > x:
            x = color_amount[item]
            win = item
    return win