import click
from program import *


@click.command()
@click.option('--gender', help='Percentage of gender. Commands: all, male, female.')
@click.option('--average_age', help='Average of age. Commands: all, male, female.')
@click.option('--popular_cities', help='The number of most popular cities. Commands: any number.')
@click.option('--popular_passwords', help='The number of most popular passwords. Commands: any number.')
@click.option('--born', multiple=True, help='Users born in between dates. Commands must be from older to newer: --born 1944-MM-DD --born 1998-MM-DD.')
@click.option('--psf', help='"Password-Security-Factor". PSF show the factor of good/bad passwords. The higher score the better. Commands: any number from 1 to 12.')
def start(gender, average_age, popular_cities, popular_passwords, born, psf):

    if gender:
        percentage_of_gender(gender)

    if average_age:
        av_age(average_age)

    if popular_cities:
        pop_cities(popular_cities)

    if popular_passwords:
        pop_pass(popular_passwords)

    if born:
        users_born_dates(born)

    if psf:
        password_security_factor(psf)


if __name__ == '__main__':
    start()
