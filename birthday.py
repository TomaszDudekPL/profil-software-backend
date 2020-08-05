import datetime
import re

from datetime import datetime


def get_current_date():
    current_day = datetime.now().day
    current_month = datetime.now().month
    return str(current_month) + "-" + str(current_day)


def clean_date_str(date_str):
    full_date = re.sub(r"T.+", "", date_str)
    return full_date


def get_number_of_days_to_birthday(current, str_from_base):
    date_format = "%Y-%m-%d"
    year = str_from_base.split('-')[0]
    fake_current = year + "-" + current
    a = datetime.strptime(fake_current, date_format)
    b = datetime.strptime(str_from_base, date_format)
    timedelta = b - a
    delta = timedelta.days

    if delta < 0:
        return 365 + delta
    else:
        return delta


def birthday(date_str):
    return get_number_of_days_to_birthday(get_current_date(), clean_date_str(date_str))
