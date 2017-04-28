import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="www-connect-conf",
    version="0.1",
    author="Limin Shen",
    author_email="limin.shen@hotmail.com",
    description=("Women Who Codes CONNECT Conf Workshop Repo."),
    license="BSD",
    keywords="workshop sample",
    url="http://packages.python.org/www-connect-conf",
    packages=['www-connect-conf', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Workshop Examples",
        "License :: OSI Approved :: BSD License",
    ],
)
