import click
from program import *


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

    if born:
        users_born_dates(born)


if __name__ == '__main__':
    start()
