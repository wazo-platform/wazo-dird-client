# xivo-dird-client

[![Build Status](https://travis-ci.org/xivo-pbx/xivo-dird-client.svg?branch=master)](https://travis-ci.org/xivo-pbx/xivo-dird-client)

A python library to connect to xivo-dird.

Usage:

```python
from xivo_dird_client import Client

c = Client('localhost', port=9489, version='0.1', timeout=3)

results = c.directories.lookup(term='alice', profile='default')
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
