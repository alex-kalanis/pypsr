PSR Container
=============

This directory holds all interfaces/classes/traits related to
[PSR-11](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-11-container.md).

Note that this is not a container of its own. It is merely an interface that
describes a container. See the specification for more details.

Installation
------------

With the rest of the package.

```bash
pip3 install pypsr
```

Usage
-----

If you need a container class loader, you can use the interface like this:

```python
from pypsr.container.interfaces import ContainerInterface


class Bar:

    def prepare_area_for_action(self) -> None:
        pass

    def get_some_data(self) -> str:
        # here return something heavier and more productive
        return 'baz'


class Foo:

    def __init__(self, container: ContainerInterface):
        self._container: ContainerInterface = container

    def get_something_from_container(self) -> str:
        klass = self._container.get(Bar)
        klass.prepare_area_for_action()
        return klass.get_some_data()

    # do something else useful
```

You can then pick one of the implementations of the interface to get a container.

If you want to implement the interface, you can require this package and
implement `pypsr.container.interfaces.ContainerInterface` in your code.
Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-11-container.md)
for details.
