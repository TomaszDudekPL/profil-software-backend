import click
from program import *
from query_db import *


@click.command()
@click.option('--gender', help='Percentage of gender. Commands: all, male, female.')
@click.option('--age', help='Average of age. Commands: all, male, female.')
@click.option('--cities', help='The number of most popular cities. Commands: any number.')
@click.option('--passwords', help='The number of most popular passwords. Commands: any number.')
@click.option('--born', multiple=True, help='Users born in between dates. Commands must be from older to newer: --born 1944-MM-DD --born 1998-MM-DD.')
@click.option('--psf', help='"Password-Security-Factor". PSF show the factor of good/bad passwords. The higher score the better. Commands: any number from 1 to 12.')
def start(gender, age, cities, passwords, born, psf):

    result = None

    if gender:
        result = percentage_of_gender(gender, db_female, db_male, db_people)

    if age:
        result = av_age(age, db_age_all, db_age_female, db_age_male)

    if cities:
        result = pop_cities(cities, db_cities)

    if passwords:
        result = pop_pass(passwords, db_pass_pop)

    if born:
        result = users_born_dates(born, db_dob)

    if psf:
        result = password_security_factor(psf, db_pass_all)

    if result:
        print(result)


if __name__ == '__main__':
    start()
