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


def percentage_of_gender(gender, db_female, db_male, db_people):

    fem = db_female()
    male = db_male()
    both = db_people()

    if gender == 'all':
        if male != 0 or fem != 0:
            per_female = (fem * 100) / both
            per_male = (male * 100) / both
            return 'female: {} %\nmale: {} %'.format(str(per_female), str(per_male))

    if gender == 'male':
        if male != 0:
            per_male = (male * 100) / both
            return 'male: {} %'.format(str(per_male))

    if gender == 'female':
        if fem != 0:
            per_female = (fem * 100) / both
            return 'female: {} %'.format(str(per_female))


def av_age(average_age, db_age_all=None, db_age_female=None, db_age_male=None):

    def get_result(msg, cb):
        sum_of_ages = 0
        result = cb()
        if result:
            num_of_all = len(result)

            for elem in result:
                sum_of_ages += elem[0]

            average = int(sum_of_ages / num_of_all)
            return msg + str(average)
        else:
            return 'NO RESULTS IN DATABASE'

    if average_age == 'all':
        return get_result('Average of age for both gender: ', db_age_all)

    if average_age == 'female':
        return get_result('Average of age for female: ', db_age_female)

    if average_age == 'male':
        return get_result('Average of age for male: ', db_age_male)


def pop_cities(num, db_cities):
    result = db_cities(num)
    str_result = ''
    if result:
        for city in result:
            str_result += 'Frequency in db: {} --> {}\n'.format(city[1], city[0])
    else:
        return 'NO RESULTS IN DATABASE'

    return str_result


def pop_pass(num, db_pass_pop):
    result = db_pass_pop(num)
    str_result = ''
    if result:
        for password in result:
            str_result += 'Frequency in db: {} --> {}\n'.format(password[1], password[0])
    else:
        return 'NO RESULTS IN DATABASE'

    return str_result


def users_born_dates(params, db_dob):
    my_params = ['', get_current_date()]

    for i in range(len(params)):
        my_params[i] = params[i]

    result = db_dob(my_params[0], my_params[1])
    str_result = ''

    if result:
        str_result += '\nUsers born between: {} and {}\n\n'.format(my_params[0], my_params[1])
        for user in result:
            str_result += clean_date_str(user[2]) + ' ' + user[0] + ' ' + user[1] + '\n'
    else:
        return '\nNo Results for these range od dates. Remember that range must start with older date.'

    return str_result


def password_security_factor(psf_str, db_pass_all):
    result = db_pass_all()
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
    str_result = '\nRESULTS:\n\n'

    if psf_str in psf_obj:
        str_result += str(psf_obj[psf_str])
        str_result += '\n\nAvailable "Password-Security-Factor" for current database: {}\n'.format(result_list)

    else:
        return '\nFor this PSF number there is NO RESULTS.\nAvailable "Password-Security-Factor" for current database: {}'.format(result_list)

    return str_result
