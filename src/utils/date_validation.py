import datetime

"""Validates if a date is in yyyy-mm-dd format"""


def date_validation(date: str) -> bool:
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
