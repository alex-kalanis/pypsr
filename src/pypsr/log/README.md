PSR Log
=======

This directory holds all interfaces/classes/traits related to
[PSR-3](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md).

Note that this is not a logger of its own. It is merely an interface that
describes a logger. See the specification for more details.

Installation
------------

With the rest of the package.

```bash
pip3 install pypsr
```

Usage
-----

If you need a logger, you can use the interface like this:

```python
from pypsr.log.interfaces import LoggerInterface


class Foo:

    def __init__(self, logger: LoggerInterface | None = None):
        self._logger: LoggerInterface | None = logger

    def do_something(self):
        if self._logger:
            self._logger.info('Doing work')

        try:
            self.do_something_else()
        except Exception as ex:
            if self._logger:
                self._logger.error('Oh no!', {'exception': ex})

    # do something useful
```

You can then pick one of the implementations of the interface to get a logger.

If you want to implement the interface, you can require this package and
implement `pypsr.log.interfaces.LoggerInterface` in your code. Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md)
for details.
