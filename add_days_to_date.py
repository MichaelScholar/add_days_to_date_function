"""Function to calculate date after set amount of days."""
from datetime import datetime
from typing import Dict

days_in_months: Dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def _is_leap_year(year: int) -> bool:
    """
    checks if year is a leap year
    :param year: Year to check
    :return: bool
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def add_days_to_date(date: str, days_to_add: int) -> str:
    """
    Adds set amount of days to a provided date.
    :param date: starting date in %d.%m.%Y format
    :param days_to_add: days to add - only positive numbers
    :return: string date in %d.%m.%Y format
    """
    if not isinstance(days_to_add, int) or days_to_add < 0:
        raise ValueError('Only positive integer numbers!')

    current_date = datetime.strptime(date, '%d.%m.%Y')
    current_year, current_month, current_day = current_date.year, current_date.month, current_date.day

    if _is_leap_year(current_date.year):
        days_in_months[2] = 29

    while True:
        if days_to_add + current_day > days_in_months[current_month]:
            days_to_add -= days_in_months[current_month]
            current_month += 1
            if current_month % 12 == 1:
                current_year += 1
                current_month = 1
                if _is_leap_year(current_year):
                    days_in_months[2] = 29
                else:
                    days_in_months[2] = 28
        else:
            current_day += days_to_add
            return datetime(current_year, current_month, current_day).strftime('%d.%m.%Y')
