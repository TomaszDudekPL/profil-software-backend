from setuptools import setup

setup(
    name='start',
    version='0.1',
    py_modules=['start'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        start=start:cli
    ''',
)
