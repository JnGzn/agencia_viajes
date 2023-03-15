from setuptools import setup

setup(
    name='agencia',
    version='1.0.0',
    packages=['agencia'],
    entry_points = {
        'console_scripts': ['agencia = agencia.__main__:main']
    }
)