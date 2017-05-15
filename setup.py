from setuptools import setup

setup(
    name = 'load_rds',
    version = '0.1',
    description = 'Load an R dataframe into Pandas',
    url = 'https://github.com/kdelrosso/R-dataframe-to-Pandas',
    author = 'Kevin DelRosso',
    author_email = 'kdelrosso@gmail.com',
    license = 'MIT',
    packages = ['load_rds'],
    # including .R script
    package_data = {'': ['*.R']},
    zip_safe = False
)