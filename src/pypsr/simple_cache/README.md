PSR Simple Cache
================

This directory holds all interfaces/classes/traits related to
[PSR-16](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-16-simple-cache.md).

Note that this is not a cache of its own. It is merely an interface that
describes a cache. See the specification for more details.

Installation
------------

With the rest of the package.

```bash
pip3 install pypsr
```

Usage
-----

If you need a simplified cache, you can use the interface like this:

```python
from pypsr.simple_cache.interfaces import CacheInterface


class Foo:

    def __init__(self, cache: CacheInterface | None = None):
        self._cache: CacheInterface | None = cache

    def get_something_cached(self, key: str = 'foo-bar'):
        if self._cache:
            if self._cache.has(key):
                return self._cache.get(key)
            # no hit
            data = self.get_something()
            self._cache.set(data)
            # return crunched data
            return data

        else:
            # no cache available
            return self.get_something()

    def get_something(self):
        # here return something heavier and more productive
        return 'baz'

        # do something else useful
```

You can then pick one of the implementations of the interface to get a cache.

If you want to implement the interface, you can require this package and
implement `pypsr.simple_cache.interfaces.CacheInterface` in your code.
Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-16-simple-cache.md)
for details.
