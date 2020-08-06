from query_db import *


def percentage_of_gender(gender):
    if gender == 'all':
        per_female = (num_of_female() * 100) / num_of_people()
        per_male = (num_of_male() * 100) / num_of_people()
        print('female: ' + str(per_female) + '%')
        print('male: ' + str(per_male) + '%')
    if gender == 'male':
        per_male = (num_of_male() * 100) / num_of_people()
        print('male: ' + str(per_male) + '%')
    if gender == 'female':
        per_female = (num_of_female() * 100) / num_of_people()
        print('female: ' + str(per_female) + '%')


def av_age(average_age):

    def get_result(msg, cb):
        sum_of_ages = 0
        result = cb()
        num_of_all = len(result)

        for elem in result:
            sum_of_ages += elem[0]

        average = int(sum_of_ages / num_of_all)
        print(msg, average)

    if average_age == 'all':
        get_result('Average of age for both gender: ', av_of_age_all)

    if average_age == 'female':
        get_result('Average of age for female: ', av_of_age_female)

    if average_age == 'male':
        get_result('Average of age for male: ', av_of_age_male)


def pop_cities(num):
    result = cities(num)
    for city in result:
        print('Frequency in db: ', city[1], '-->', city[0])


def pop_pass(num):
    result = passwords(num)
    for password in result:
        print('Frequency in db: ', password[1], '-->', password[0])


def users_born_dates(params):
    result = dob(params[0], params[1])
    if result:
        print('Users born between: ', params[0], ' and: ', params[1], ': ')
    else:
        print('No Results for these range od dates. Remember that range must start with older date.')
    for user in result:
        print('First Name: ', user[0], 'Last Name: ', user[1], 'Date: ', user[2])
