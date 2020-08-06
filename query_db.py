from db import query_db

number_of_people = 'SELECT "gender" FROM persons'
number_of_female = 'SELECT "gender" FROM persons WHERE "gender"="female"'
number_of_male = 'SELECT "gender" FROM persons WHERE "gender"="male"'
average_of_age_all = 'SELECT "dob.age" FROM persons'
average_of_age_female = 'SELECT "dob.age" FROM persons WHERE "gender"="female"'
average_of_age_male = 'SELECT "dob.age" FROM persons WHERE "gender"="male"'
popularity_of_cities = 'SELECT "location.city", COUNT(*) AS "location.city" FROM persons GROUP BY "location.city" ORDER BY COUNT(*) DESC LIMIT "{}"'
popularity_of_passwords = 'SELECT "login.password", COUNT(*) AS "login.password" FROM persons GROUP BY "login.password" ORDER BY COUNT(*) DESC LIMIT "{}"'
date_of_birth = 'SELECT "name.first", "name.last", "dob.date" FROM persons WHERE "dob.date" BETWEEN "{}" and "{}" ORDER BY "dob.date" DESC'


def num_of_people():
    res = query_db(number_of_people)
    return len(res)


def num_of_female():
    res = query_db(number_of_female)
    return len(res)


def num_of_male():
    res = query_db(number_of_male)
    return len(res)


def av_of_age_all():
    res = query_db(average_of_age_all)
    return res


def av_of_age_female():
    res = query_db(average_of_age_female)
    return res


def av_of_age_male():
    res = query_db(average_of_age_male)
    return res


def cities(param):
    res = query_db(popularity_of_cities.format(param))
    return res


def passwords(param):
    res = query_db(popularity_of_passwords.format(param))
    return res


def dob(start, end):
    res = query_db(date_of_birth.format(start, end))
    return res
