#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


class DjangoTest(TestCommand):

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import django
        from django.conf import settings
        from django.test.utils import get_runner
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(['tests'])
        sys.exit(bool(failures))


setup(
    name='django_chatwork',
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
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=['Django'],
    cmdclass={'test': DjangoTest},
)
