"""Control function with add_days_to_date"""

import datetime
from typing import Union, List


def add_days_to_date(date: Union[str, List[int]], days: int) -> datetime:
    """
    :param date: date in a %d-%m-%Y format (eg. 05.02.2022)
    :param days: days to add
    :return: datetime object
    """
    input_date = datetime.datetime.strptime(date, '%d.%m.%Y')
    return datetime.date.fromtimestamp(input_date.timestamp() + days * 24 * 60 * 60).strftime('%d.%m.%Y')
