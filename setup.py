#!/usr/bin/env python
import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-chatwork',
    url='https://github.com/kacchan822/django-chatwork',
    version='0.1.0',
    description='Chatwork integration for Django',
    long_description=README,
    author='Katsuya SAITO',
    author_email='hello@skatsuya.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=find_packages(exclude=['tests', ]),
    include_package_data=True,
    install_requires=(
        'Django>=1.11.0',
    ),
)
