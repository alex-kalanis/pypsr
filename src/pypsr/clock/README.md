PSR Clock
=========

This directory holds all interfaces/classes/traits related to
[PSR-20](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-20-clock.md).

Note that this is not a clock of its own. It is merely an interface that
describes a clock. See the specification for more details.

Installation
------------

With the rest of the package.

```bash
pip3 install pypsr
```

Usage
-----

If you need a clock, you can use the interface like this:

```python
from pypsr.clock.interfaces import ClockInterface


class Foo:

    def __init__(self, clock: ClockInterface):
        self._clock: ClockInterface = clock

    def current_hour(self) -> int:
        return self._clock.now().hour

    def save_time_to_file(self) -> None:
        with open('x.txt', 'w+') as fh:
            fh.write(str(int(self._clock.now().timestamp())) + '\n')
            fh.close()

    # do something else useful
```

You can then pick one of the implementations of the interface to get a clock.

If you want to implement the interface, you can require this package and
implement `pypsr.clock.interfaces.ClockInterface` in your code.
Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-20-clock.md)
for details.
