import click
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

    if average_age == "all":
        sum_of_ages = 0
        result = av_of_age_all()
        num_of_all = len(result)

        for elem in result:
            sum_of_ages += elem[0]

        average = int(sum_of_ages / num_of_all)
        print('Average of age for both gender: ', average)

    if average_age == "female":
        sum_of_ages = 0
        result = av_of_age_female()
        num_of_all = len(result)

        for elem in result:
            sum_of_ages += elem[0]

        average = int(sum_of_ages / num_of_all)
        print('Average of age for female: ', average)

    if average_age == "male":
        sum_of_ages = 0
        result = av_of_age_male()
        num_of_all = len(result)

        for elem in result:
            sum_of_ages += elem[0]

        average = int(sum_of_ages / num_of_all)
        print('Average of age for male: ', average)


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


@click.command()
@click.option('--gender', default=None, help='Percentage of gender. Commands: all, male, female.')
@click.option('--average_age', default=None, help='Average of age. Commands: all, male, female.')
@click.option('--popular_cities', default=None, help='The most popular cities. Commands: any number')
@click.option('--popular_passwords', default=None, help='The most popular password. Commands: any number')
@click.option('--born', default=None, multiple=True, help='Users born in between dates. Commands must be from older to newer: --born 1983-MM-DD --born 2015-MM-DD')
def start(gender, average_age, popular_cities, popular_passwords, born):

    if gender:
        percentage_of_gender(gender)

    if average_age:
        av_age(average_age)

    if popular_cities:
        pop_cities(popular_cities)

    if popular_passwords:
        pop_pass(popular_passwords)

    if dob:
        users_born_dates(born)


if __name__ == '__main__':
    start()
