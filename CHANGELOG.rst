CHANGELOG
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <http://keepachangelog.com/en/1.0.0/>`__ and this project
adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`__.

[Unreleased] - 0000-00-00
-------------------------

Added
~~~~~

* ...

Changed
~~~~~~~

* ...

Deprecated
~~~~~~~~~~

* ...

Removed
~~~~~~~

* ...

Fixed
~~~~~

* ...

Security
~~~~~~~~

* ...


[0.6.0] - 2021-02-07
-------------------------

Changed
~~~~~

* Support Django 2.2, 3.0, 3.1 and droped support Django 1.10

Fixed
~~~~~

* RemovedInDjango40Warning: force_text() is deprecated in favor of force_str().


[0.5.0] - 2019-09-02
-------------------------

Added
~~~~~

* function **delete_message**


[0.4.0] - 2018-06-06
-------------------------

Added
~~~~~

* API methods:update, delete, read and unread message

Changed
~~~~~~~

* Message notation for all members in room


[0.3.0] - 2017-11-17
-------------------------

Still Development State

Added
~~~~~~~

* function **create_task**

Fixed
~~~~~~~

* Cannot mentione to all member in room even if to_all = True.
* Lost message text sending info style message.


[0.2.0] - 2017-10-06
-------------------------

Still Development State

Changed
~~~~~~~

* **DummyBackend** returns example dict that values based on Chatwork API document instead of empty dict.
* Set **CHATWORK_API_BACKEND** to class name string -- 'chatwork.backends.dummy.DummyBackend' or 'chatwork.backends.http.UrllibBackend'.


[0.1.2] - 2017-09-27
-------------------------

Initial Release (Development State)
