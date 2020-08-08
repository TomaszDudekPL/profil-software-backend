from query_db import *
from birthday import clean_date_str
from datetime import datetime


def get_current_date():

    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    if current_month < 10:
        current_month = '0' + str(current_month)
    if current_day < 10:
        current_day = '0' + str(current_day)

    return str(current_year) + "-" + str(current_month) + "-" + str(current_day)


def percentage_of_gender(gender):

    fem = num_of_female()
    male = num_of_male()
    both = num_of_people()

    if gender == 'all':
        if male != 0 or fem != 0:
            per_female = (fem * 100) / both
            per_male = (male * 100) / both
            print('female: ' + str(per_female) + '%')
            print('male: ' + str(per_male) + '%')

    if gender == 'male':
        if male != 0:
            per_male = (male * 100) / both
            print('male: ' + str(per_male) + '%')

    if gender == 'female':
        if fem != 0:
            per_female = (fem * 100) / both
            print('female: ' + str(per_female) + '%')


def av_age(average_age):

    def get_result(msg, cb):
        sum_of_ages = 0
        result = cb()
        if result:
            num_of_all = len(result)

            for elem in result:
                sum_of_ages += elem[0]

            average = int(sum_of_ages / num_of_all)
            print(msg, average)
        else:
            print('NO RESULTS IN DATABASE')

    if average_age == 'all':
        get_result('Average of age for both gender: ', av_of_age_all)

    if average_age == 'female':
        get_result('Average of age for female: ', av_of_age_female)

    if average_age == 'male':
        get_result('Average of age for male: ', av_of_age_male)


def pop_cities(num):
    result = cities(num)
    if result:
        for city in result:
            print('Frequency in db: ', city[1], '-->', city[0])
    else:
        print('NO RESULTS IN DATABASE')


def pop_pass(num):
    result = passwords_popularity(num)
    if result:
        for password in result:
            print('Frequency in db: ', password[1], '-->', password[0])
    else:
        print('NO RESULTS IN DATABASE')


def users_born_dates(params):
    my_params = ['', get_current_date()]

    for i in range(len(params)):
        my_params[i] = params[i]

    result = dob(my_params[0], my_params[1])

    if result:
        print('\nUsers born between: ', my_params[0], 'and', my_params[1], '\n')
        for user in result:
            print(clean_date_str(user[2]), user[0], user[1])
    else:
        print('\nNo Results for these range od dates. Remember that range must start with older date.')


def password_security_factor(psf_str):
    result = passwords()
    psf_obj = {}

    if result:
        for password in result:
            # 1. Estimate "Password-Security-Factor" for each password in database.
            psf = 0
            if any(c.islower() for c in password[0]):
                psf += 1
            if any(c.isupper() for c in password[0]):
                psf += 2
            if any(char.isdigit() for char in password[0]):
                psf += 1
            if len(password[0]) >= 8:
                psf += 5
            if any(not c.isalnum() for c in password[0]):
                psf += 3

            # 2. Create dict with "Password-Security-Factor" and corresponding to them lists of passwords.
            if str(psf) in psf_obj:
                psf_obj[str(psf)].append(password[0])

            else:
                psf_obj[str(psf)] = []
                psf_obj[str(psf)].append(password[0])

    else:
        print('NO RESULTS IN DATABASE')

    # 3. Presentation of results.
    result_list = [*psf_obj]
    result_list.sort()

    if psf_str in psf_obj:
        print('\nRESULTS:\n')
        print(psf_obj[psf_str])
        print('\nAvailable "Password-Security-Factor" for current database: ', result_list, '\n')

    else:
        print('\nFor this PSF number there is NO RESULTS.')
        print('\nAvailable "Password-Security-Factor" for current database: ', result_list)
