# Profile-Software
## Database Analyzer

According to the requirements of the task : [Link to task](https://git.profil-software.com/recruitment-july-2020/backend/-/blob/master/README.md)


### How to start:

Clone project and install required dependencies:

Library: "Setuptools" [Link to official site](https://packaging.python.org/tutorials/installing-packages/)

```pip install setuptools```

Library: "Click" [Link to documentation](https://click.palletsprojects.com/en/7.x/)

```pip install click```

Library "py.test" [Link to documentation](https://docs.pytest.org/en/latest/contents.html)

```pip install -U pytest```

### When dependencies are ready:

1. Create database (from file persons.json)

      In terminal run: ```python create_base.py```

2. When database is ready, you can start using program:

      For example: ```python start.py --gender female``` will give you percentage of all women in database persons

    All available options to use:
    
    Options:
    
        --gender             Percentage of gender. Commands: all, male, female.
  
        --age                Average of age. Commands: all, male, female.
        
        --cities             The number of most popular cities. Commands: any number.
        
        --passwords          The number of most popular passwords. Commands: any number.
        
        --born               Users born in between dates. Commands must be from older to newer: --born 1944-MM-DD --born 1998-MM-DD.
                             One parameter is possible then you can see records from your argument to the 1998-09-12 (the last date in current base).
        
        --psf                "Password-Security-Factor". PSF show the factor of good/bad passwords. The higher score the better. Commands: any number from 1 to 12.
        
        --help               Show all available options.


### For testing:

Just use command: ```pytest -v``` for all tests.

If you want to run only some part of tests choose one from above options. For example: ```pytest -v -k gender```

 