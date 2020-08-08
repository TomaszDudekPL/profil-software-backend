import requests
import re
from birthday import birthday
from db import run_database


def request_for_data(url):
    res = requests.get(url)
    print(res.status_code)
    data = res.json()
    return data


def clean_phone_str(phone_str):
    return re.sub(r"\W", "", phone_str)


def prepare_data_for_database(obj):
    # Prepare list of objects for database
    list_of_object = obj['results']
    for ob in list_of_object:
        ob['phone'] = clean_phone_str(ob['phone'])
        ob['cell'] = clean_phone_str(ob['cell'])
        ob['dob']['days_to_birthday'] = birthday(ob['dob']['date'])
        del ob['picture']
    return list_of_object


arr = []
if __name__ == '__main__':
    arr = prepare_data_for_database(request_for_data('https://randomuser.me/api/?results=1000'))
    run_database(arr)
