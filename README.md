# xivo-dird-client

[![Build Status](https://travis-ci.org/xivo-pbx/xivo-dird-client.svg?branch=master)](https://travis-ci.org/xivo-pbx/xivo-dird-client)

A python library to connect to xivo-dird.

Usage:

```python
from xivo_dird_client import Client

c = Client('localhost', port=9489, version='0.1', timeout=3)

results = c.directories.headers(term='alice', profile='default', token='my-valid-token')
results = c.directories.lookup(term='alice', profile='default', token='my-valid-token')

results = c.directories.favorites(profile='default', token='my-valid-token')
c.directories.new_favorite('my-directory', 'contact-in-my-directory', token='my-valid-token')
c.directories.remove_favorite('my-directory', 'contact-in-my-directory', token='my-valid-token')

results = c.directories.personal(profile='default', token='my-valid-token')

personal = c.personal.list(token='my-valid-token')
my_contact = {
    'firstname': 'Alice',
    'lastname': 'Scylla'
}
my_new_contact = c.personal.create(my_contact, token='my-valid-token')
personal = c.personal.delete(my_new_contact['id'], token='my-valid-token')
```


## How to implement a new command

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
