xivo-dird-client
================

[![Build Status](https://travis-ci.org/wazo-pbx/xivo-dird-client.svg?branch=master)](https://travis-ci.org/wazo-pbx/xivo-dird-client)

A python library to connect to xivo-dird.

Usage:

```python
from xivo_dird_client import Client

c = Client('localhost', port=9489, version='0.1', timeout=3)

results = c.directories.headers(term='alice', profile='default', token='my-valid-token')
results = c.directories.lookup(term='alice', profile='default', token='my-valid-token')
results = c.directories.reverse(exten='4185551234', profile='default', token='my-valid-token')

results = c.directories.favorites(profile='default', token='my-valid-token')
c.directories.new_favorite('my-directory', 'contact-in-my-directory', token='my-valid-token')
c.directories.remove_favorite('my-directory', 'contact-in-my-directory', token='my-valid-token')

results = c.directories.personal(profile='default', token='my-valid-token')

personal = c.personal.list(token='my-valid-token')
csv_text = c.personal.export_csv(token='my-valid-token')  # None if no personal contacts
csv_text = '''firstname,lastname
Alice,Scylla
'''
import_result = c.personal.import_csv(csv_text, encoding='utf-8', token='my-valid-token')
c.personal.purge(token='my-valid-token')
my_contact = {
    'firstname': 'Alice',
    'lastname': 'Scylla'
}
my_new_contact = c.personal.create(my_contact, token='my-valid-token')
contact_id = my_new_contact['id']
personal = c.personal.get(contact_id, token='my-valid-token')
my_contact = {
    'firstname': 'Alice',
    'lastname': 'Scylla',
    'company': 'acme,'
}
new_personal = c.personal.edit(contact_id, my_contact, token='my-valid-token')
c.personal.delete(my_new_contact['id'], token='my-valid-token')

c.phonebook.import_csv(token='my-valid-token', tenant='default', phonebook_id=7, csv_text=csv_text, encoding='utf-8')
```


How to implement a new command
------------------------------

Someone trying to implement a new command to the client would have to implement
a new class, sub-classing the RESTCommand (available in
xivo-lib-rest-client). The new class must be in the setup.py in the entry points
under dird_client.commands. The name of the entry point is used as the handle on
the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'dird_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```

Running unit tests
------------------

```
apt-get install libpq-dev python-dev libffi-dev libyaml-dev
pip install tox
tox --recreate -e py27
```
