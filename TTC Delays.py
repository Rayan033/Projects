"""CSC110 Fall 2024 Assignment 2, Part 2: Subway Delays Revisited

Module Description
==================
This module contains the data classes and functions you should complete for Part 2.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC110 Teaching Team
"""
import csv
import datetime
from dataclasses import dataclass


###############################################################################
# The new data class
###############################################################################
@dataclass
class Delay:
    """A data type representing a specific subway delay instance.

    This corresponds to one row of the tabular data found in ttc-subway-delays.csv.

    Attributes:
    date: the date of the delay
    time: the time of the delay
    day: the day of the week the delay occurred
    Station: the name of the station where the delay occurred
    Code: the delay code representing the type of delay
    min_delay: the minimum amount of time the delay lasted in minutes
    min_gap: the minimum gap time between trains in minutes
    bound: the direction of travel
    line: the specific subway line in which the delay occurred
    vehicle: the vehicle ID number involved in the delay

    Representation Invariants:
    0 <= min_delay
    0 <= min_gap

    """
    date: datetime.date
    time: datetime.time
    day: str
    station: str
    code: str
    min_delay: int
    min_gap: int
    bound: str
    line: str
    vehicle: int


def read_csv_file(filename: str) -> tuple[list[str], list[Delay]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of Delays.

    Note: you must complete process_row below and use it as a helper function
    in this function body.

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)

    >>> read_csv_file('oneline.csv')
    (['Date', 'Time', 'Day', 'Station', 'Code', 'Min Delay', 'Min Gap', 'Bound', \
'Line', 'Vehicle'], [Delay(date=datetime.date(2014, 1, 1), time=datetime.time(0, 21), \
day='Wednesday', station='VICTORIA PARK STATION', code='MUPR1', min_delay=55, \
min_gap=60, bound='W', line='BD', vehicle=5111)])
    """
    with open(filename) as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [process_row(row) for row in reader]
    return headers, data


def process_row(row: list[str]) -> Delay:
    """Convert a row of subway delay data to Delay object.

    Notes:
    - You can use int(...) to convert from a string to an integer
    - You must complete the str_to_date and str_to_time functions below
      and use them here.

    Preconditions:
        - row has the correct format for the TTC subway delay data set

    >>> process_row(['01/01/2014', '00:21', 'Wednesday', 'VICTORIA PARK STATION', 'MUPR1', '55', '60', 'W', 'BD', \
'5111'])
    Delay(date=datetime.date(2014, 1, 1), time=datetime.time(0, 21), \
day='Wednesday', station='VICTORIA PARK STATION', code='MUPR1', min_delay=55, \
min_gap=60, bound='W', line='BD', vehicle=5111)
    """
    return Delay(date=str_to_date(row[0]), time=str_to_time(row[1]), day=row[2], station=row[3], code=row[4],
                 min_delay=int(row[5]), min_gap=int(row[6]), bound=row[7], line=row[8], vehicle=int(row[9]))


def str_to_date(date_string: str) -> datetime.date:
    """Convert a string in mm/dd/yyyy format to a datetime.date.

    Hints:
    1. You can use str.split(date_string, '/') to first obtain
       the three strings corresponding to month, day, and year separately.
    2. Create a new datetime.date value by calling this type on three arguments:
       datetime.date(year, month, day).

    Preconditions:
    - date_string has format mm/dd/yyyy

    >>> str_to_date('01/01/2014')
    datetime.date(2014, 1, 1)
    """
    split_date = date_string.split('/')
    return datetime.date(int(split_date[2]), int(split_date[0]), int(split_date[1]))


def str_to_time(time_string: str) -> datetime.time:
    """Convert a time string with hours and minutes to a datetime.time.

    Preconditions:
    - time_string has format HH:mm, where the hours are specified in 24-hour format (from 00 to 23).

    Similar hint as str_to_date. datetime.time takes two arguments:
    hour and minute, in that order.

    >>> str_to_time('00:21')
    datetime.time(0, 21)
    """
    split_time = time_string.split(':')
    return datetime.time(int(split_time[0]), int(split_time[1]))


###############################################################################
# Operating on the data
###############################################################################
def longest_delay(data: list[Delay]) -> int:
    """Return the longest delay in the given data.

    Notes:
    - As stated in the handout, you must use the accumulator pattern for this function.

    Preconditions:
    - data != []

    >>> delay_data = read_csv_file('twolines.csv')
    >>> longest_delay(delay_data[1])
    55
    """
    long_delay = 0
    for delay in data:
        if delay.min_delay > long_delay:
            long_delay = delay.min_delay
    return long_delay


def average_delay(data: list[Delay]) -> float:
    """Return the average subway delay in data.

    Notes:
    - As stated in the handout, you must use the accumulator pattern for this function.

    Preconditions:
    - data != []

    >>> delay_data = read_csv_file('twolines.csv')
    >>> average_delay(delay_data[1])
    29.0
    """
    total_delay = 0
    num_delays = 0

    for delay in data:
        total_delay += delay.min_delay
        num_delays += 1
    return total_delay / num_delays if num_delays > 0 else 0.0


def num_delays_by_month(data: list[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Notes:
    - As stated in the handout, you must use the accumulator pattern for this function.

    Preconditions:
    - 0 < month <= 12
    - 2014 <= year <= 2019

    >>> delay_data = read_csv_file('twolines.csv')
    >>> num_delays_by_month(delay_data[1], 2014, 1)
    2
    >>> num_delays_by_month(delay_data[1], 2014, 2)
    0
    """
    total_delays = 0
    for delay in data:
        if delay.date.year == year and delay.date.month == month:
            total_delays += 1
    return total_delays


if __name__ == '__main__':
    # DO NOT MODIFY ANY CODE BELOW (You can and should comment/uncomment them out for testing purposes though)
    import doctest

    #
    doctest.testmod(verbose=True)
    #
    import python_ta

    #
    python_ta.check_all(config={
        'disable': ['R0902'],
        'extra-imports': ['csv', 'datetime'],
        'allowed-io': ['read_csv_file'],
        'max-line-length': 120
    })
