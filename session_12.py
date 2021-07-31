import datetime
import random
from collections import namedtuple
from datetime import date
from functools import wraps
from statistics import mode
from time import perf_counter

from faker import Faker
from numpy import random

# Using Faker create 1 fake profile
fake = Faker()
fake.profile()

# To make a named tuple named Profile with the keys in fake profile as fields
Profile = namedtuple('Profile', fake.profile().keys())


# Decorator for the execution time for named tuples and dictionary
def timed(fn):
    """ Decorator for run time of a function."""

    @wraps(fn)
    def inner(*args, **kwargs):
        """ Inner function - calculate the time."""
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_elapsed = (end - start)
        return time_elapsed, result

    return inner


# Question1

def init_profiles_using_namedtuple(no_profiles: int):
    """Creating fake profiles for n number of people given as parameter using namedTuples"""
    profiles = []
    Profile = namedtuple('Profile', fake.profile().keys())
    for _ in range(no_profiles):
        profiles.append(Profile(**fake.profile()))
    return profiles


@timed
def oldest_person_nt(all_profile_nt: namedtuple) -> float:
    """This function finds the oldest person & calculates the duration. Returns minimum birthdate and time. """
    """Param: all_profile_nt: Named tuple containing all profiles"""
    value = min(all_profile_nt, key=lambda v: v[-1])
    date_today = datetime.date.today()
    age = (date_today - value.birthdate).days
    return int(age / 365)


@timed
def average_age_nt(all_profile_nt: namedtuple) -> tuple:
    """Function to finds the average age of the person and calculated duration to perform that operation. \
    Returns average age and time."""
    """Param: all_profile_nt: Named tuple containing all profiles"""
    today = date.today()
    value = sum(map(lambda v: today.year - v[-1].year - ((today.month, today.day) < (
        v[-1].month, v[-1].day)), all_profile_nt)) / len(all_profile_nt)
    return value


@timed
def average_coordinates_nt(all_profile_nt: namedtuple) -> tuple:
    """Function to finds average coordinates & calculates duration to perform that operation. \
    Returns average coordinates and time."""
    """Param: all_profile_nt: Named tuple containing all profiles"""
    x, y = sum(map(lambda t: t[0], map(lambda v: v[4], all_profile_nt))) / len(all_profile_nt), sum(
        map(lambda t: t[1], map(lambda v: v[4], all_profile_nt))) / len(all_profile_nt)
    return x, y


@timed
def max_blood_group_nt(all_profile_nt: namedtuple) -> tuple:
    """Function uses the mode function defined in statistics library to find the most occurred blood group from the list. \
    The list is generated using the lambda function and returned to the mode function as a parameters. \
    The code is then timed and the result and time is sent back."""
    """Param:all_profile_nt: Named tuple containing all profiles"""
    blood_group = mode(list(map(lambda v: v[5], all_profile_nt)))
    return blood_group


def time_nt(fk_profile_nt: namedtuple, n: int) -> 'float':
    ti = 0
    for _ in range(n):
        total_exec_time_nt = oldest_person_nt(fk_profile_nt)[0] + average_age_nt(fk_profile_nt)[
            0] + average_coordinates_nt(fk_profile_nt)[0] + max_blood_group_nt(fk_profile_nt)[0]
        ti += total_exec_time_nt
    return ti / n


# Question2

# Converting the Profile Data generated into Dictionary

def named_tuple_dict(all_profile_nt: namedtuple) -> dict:
    return {'Profile' + str(_): t._asdict() for _, t in enumerate(all_profile_nt)}


@timed
def oldest_person_dc(all_profile_dict: dict) -> float:
    """Function finds the oldest person & calculates the duration to perform that operation. \
    Returns birthdate and time."""
    """Param:all_profile_dc: dictionary containing all profiles"""
    value = min(all_profile_dict.values(), key=lambda v: v['birthdate'])
    date_today = datetime.date.today()
    age = (date_today - value['birthdate']).days
    return int(age / 365)


@timed
def average_age_dc(all_profile_dict: dict) -> float:
    """Function finds the average age & calculates the duration to perform that operation. \
    Returns Age and time."""
    """Param:all_profile_dc: Dictionary containing all profiles"""
    today = date.today()
    value = sum(map(lambda v: today.year - v['birthdate'].year - ((today.month, today.day) < (
        v['birthdate'].month, v['birthdate'].day)), all_profile_dict.values())) / len(all_profile_dict)
    return value


@timed
def average_coordinates_dc(all_profile_dict: dict) -> tuple:
    """Function finds the average coordinates & calculates the duration to perform that operation. \
    Returns average coordinates time."""
    """Param:all_profile_dc: dictionary containing all profiles"""
    x, y = sum(map(lambda t: t[0], map(lambda v: v['current_location'], all_profile_dict.values()))) / len(
        all_profile_dict.values(
        )), sum(map(lambda t: t[1], map(lambda v: v['current_location'], all_profile_dict.values()))) / len(
        all_profile_dict.values())
    return x, y


@timed
def max_blood_group_dc(all_profile_dict: dict) -> tuple:
    """Function uses the mode function defined in statistics library to find the most occurred blood group from the list. \
    The list is generated using the lambda function and returned to the mode function as a parameters. \
    The code is then timed and the result and time is sent back."""
    """Param:all_profile_dc: dictionary containing all profiles"""
    value = mode(
        list(map(lambda v: v['blood_group'], all_profile_dict.values())))
    return value


def time_dc(fk_profile_dict: dict, n: int) -> 'float':
    ti = 0
    for _ in range(n):
        total_exec_time_dc = oldest_person_dc(fk_profile_dict)[0] + average_age_dc(fk_profile_dict)[
            0] + average_coordinates_dc(fk_profile_dict)[0] + max_blood_group_dc(fk_profile_dict)[0]
        ti += total_exec_time_dc
    return ti / n


# Question3

# Returns a Symbol of the the Company
def symbol(string: str) -> str:
    """Returns joined string if characters are upper case"""
    length_ = len(string)
    p1 = random.randint(1, length_ - 1, 2)
    chars = []
    for char in string:
        chars.append(char)
    chars[p1[0]] = chars[p1[0]].upper()
    chars[p1[1]] = chars[p1[1]].upper()
    return ''.join(x for x in chars if x.isupper()) + str(random.randint(9))


def stock_market(no_profiles: int) -> tuple:
    """1. Creates a Fake stock data set for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). \
    2. Assign a random weight to all the companies. \
    3. Calculates and show what \
    value stock market started at, \
    what was the highest value during the day \
    and where did it end."""
    all_companies = []
    Stocks = namedtuple("Stocks", 'name symbol open high close company_weight')
    mk_value_ = random.uniform(1000, 50000, 100)
    wts_ = random.uniform(0, 1, 100)
    wts_ = wts_ / sum(wts_)

    for _ in range(100):
        name = fake.company()
        open_ = round(mk_value_[_] * wts_[_], 2)
        close = round(open_ * random.uniform(0.7, 1.15), 2)
        high = round(open_ * random.uniform(0.85, 1.15), 2)
        if high < open_:
            high = open_
        if high < close:
            high = close

        all_companies.append(
            Stocks(name=name, symbol=symbol(name), open=open_, high=round(high, 2), close=round(close, 2),
                   company_weight=round(wts_[_], 4)))

    stock_index = round(
        sum(x.open * x.company_weight for x in all_companies), 4)
    highest_for_day = round(
        sum(x.high * x.company_weight for x in all_companies), 2)
    lowest_close_for_day = round(
        sum(x.close * x.company_weight for x in all_companies), 2)

    return sorted(all_companies, key=lambda x: x.symbol), stock_index, highest_for_day, lowest_close_for_day
