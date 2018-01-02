from distutils.core import setup
from setuptools import find_packages

import rrpi


setup(
    name='rrpi',
    version=rrpi.__VERSION__,
    packages=find_packages(),
    license=open('LICENSE.txt').read(),
    long_description=open('README.md').read(),
    data_files=[],
    install_requires=[
        'paramiko',
    ],
)
