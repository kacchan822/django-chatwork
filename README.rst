===============
django-chatwork
===============

.. image:: https://travis-ci.org/kacchan822/django-chatwork.svg?branch=master
    :target: https://travis-ci.org/kacchan822/django-chatwork
    :alt: Travis CI

.. image:: https://coveralls.io/repos/github/kacchan822/django-chatwork/badge.svg?branch=master
    :target: https://coveralls.io/github/kacchan822/django-chatwork?branch=master
    :alt: COVERALLS

.. image:: https://codeclimate.com/github/kacchan822/django-chatwork/badges/gpa.svg
   :target: https://codeclimate.com/github/kacchan822/django-chatwork
   :alt: Code Climate

.. image:: https://codeclimate.com/github/kacchan822/django-chatwork/badges/issue_count.svg
   :target: https://codeclimate.com/github/kacchan822/django-chatwork
   :alt: Issue Count

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/kacchan822/django-chatwork/master/LICENSE
   :alt: LICENSE MIT


**django-chatwork** is Chatwork integration for Django.


Requirement
============

* Python >= 3.5
* Django >= 1.11


Quick start
============

1. Install by pip :: 

    # instal from PyPI
    pip install django-chatwork

    # install from github master branch
    pip install -U https://github.com/kacchan822/django-chatwork/archive/master.tar.gz


2. Add "chatwork" to INSTALLED_APPS :: 

    INSTALLED_APPS = [
        ...
        'chatwork',
        ...
    ]


3. Set Valuse in settings :: 

    # You have to set this
    CHATWORK_API_TOKEN = 'youre api token'

    # You don't have to usually set this
    CHATWORK_API_ENDPOINT_BASE =  'https://api.chatwork.com/v2' # default
    CHATWORK_API_BACKEND = 'http' # default if DEBUG = False
                                  # if DEBUG = True, the value set 'dummy' as default
    CHATWORK_API_FAIL_SILENTLY = None   # default


4. Use age :: 

    from chatwork import send_message

    ...

    # send message to room_id = 123456
    send_chatwork('message text hear', 123456)

    # send message to room_id = 123456 with [To:] for all members
    send_chatwork('message text hear', 123456, to_all=True)

    # send message to room_id = 123456 with INFO format
    # INFO format contains [To:] for all users
    send_chatwork('message text hear', 123456, title='info title')

    ...


Acknowledgements
=================
