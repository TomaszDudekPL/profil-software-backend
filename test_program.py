import pytest
import program as p
from mock_query_db import *


@pytest.mark.gender
def test_percentage_of_gender_option_all():
    assert p.percentage_of_gender('all', mock_db_female, mock_db_male, mock_db_people) == 'female: 45.0 %\nmale: 55.0 %'


@pytest.mark.gender
def test_percentage_of_gender_option_female():
    assert p.percentage_of_gender('female', mock_db_female, mock_db_male, mock_db_people) == 'female: 45.0 %'


@pytest.mark.gender
def test_percentage_of_gender_option_male():
    assert p.percentage_of_gender('male', mock_db_female, mock_db_male, mock_db_people) == 'male: 55.0 %'


@pytest.mark.age
def test_av_age_option_all():
    assert p.av_age('all', mock_db_age_all) == 'Average of age for both gender: 50'


@pytest.mark.age
def test_av_age_option_female():
    assert p.av_age('female', mock_db_age_all, mock_db_age_female) == 'Average of age for female: 50'


@pytest.mark.age
def test_av_age_option_male():
    assert p.av_age('male', mock_db_age_all, mock_db_age_female, mock_db_age_male) == 'Average of age for male: 50'


@pytest.mark.cities
def test_pop_cities():
    res = 'Frequency in db: 5 --> Devonport\nFrequency in db: 5 --> Ballarat\nFrequency in db: 4 --> Whanganui\n'
    assert p.pop_cities(3, mock_db_cities) == res


@pytest.mark.passwords
def test_pop_pass():
    res = 'Frequency in db: 3 --> lancer\nFrequency in db: 3 --> curious\nFrequency in db: 3 --> cherries\n'
    assert p.pop_pass(3, mock_db_pass_pop) == res


@pytest.mark.born
def test_users_born_dates():
    res = '\nUsers born between: 1944-06-12 and 1944-10-12\n\n1944-08-31 Georgia Harris\n1944-09-06 Laura Holt\n1944-09-20 Maria Roberts\n1944-10-02 Priscilla Knight\n'
    assert p.users_born_dates(['1944-06-12', '1944-10-12'], mock_db_dob) == res


@pytest.mark.psf
def test_password_security_factor_result():
    res = '''\nRESULTS:\n\n['asdT?f123']\n\nAvailable "Password-Security-Factor" for current database: ['12']\n'''
    assert p.password_security_factor('12', mock_db_pass_all_result) == res


@pytest.mark.psf
def test_password_security_factor_no_result():
    res = '''\nFor this PSF number there is NO RESULTS.\nAvailable "Password-Security-Factor" for current database: ['12']'''
    assert p.password_security_factor('3', mock_db_pass_all_result) == res
