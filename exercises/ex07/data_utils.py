"""Dictionary related utility functions."""

__author__ = "730488173"

from csv import DictReader


# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values ina single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    for item in table:
        column: list[str] = table[item]
        vals: list[str] = []
        if rows > len(table):
            for item2 in column:
                vals.append(item2)
            result[item] = vals
        else:
            i: int = 0
            while i < rows:
                vals.append(column[i])
                i = i + 1
            result[item] = vals
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = table[item]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new coumn based table wiht two column based tables combined."""
    result: dict[str, list[str]] = {}
    for item in first:
        result[item] = first[item]
    for item in second:
        if item in result:
            vals: list[str] = result[item]
            for stats in second[item]:
                vals.append(stats)
            result[item] = vals
        else:
            result[item] = second[item]
    return result


def count(freq: list[str]) -> dict[str, int]:
    """Given a list, produces a dictionary where each key is a unique value in the given list and each value associated is the amount of times it appeared initiallly."""
    result: dict[str, int] = {}
    for item in freq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
