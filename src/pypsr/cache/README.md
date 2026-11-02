PSR Cache
=========

This directory holds all interfaces/classes/traits related to
[PSR-6](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-6-cache.md).

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

If you need a cache, you can use the interface like this:

```python
from pypsr.cache.interfaces import CacheItemPoolInterface


class Foo:

    def __init__(self, cache: CacheItemPoolInterface | None = None):
        self._cache_pool: CacheItemPoolInterface | None = cache

    def get_something_cached(self, key: str = 'foo-bar'):
        if self._cache_pool:
            cached = self._cache_pool.get_item(key)
            if cached.is_hit():
                return cached.get()
            # no hit
            data = self.get_something()
            cached.set(data)
            # example with direct save
            self._cache_pool.save(cached)
            # return crunched data
            return data

        else:
            # no cache available
            return self.get_something()

    def get_something_cached_deferred_save(self, key: str = 'foo-bar'):
        if self._cache_pool:
            cached = self._cache_pool.get_item(key)
            if cached.is_hit():
                return cached.get()
            # no hit
            data = self.get_something()
            cached.set(data)
            # example with deferred save
            self._cache_pool.save_deferred(cached)
            self._cache_pool.commit()
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
implement `pypsr.cache.interfaces.CacheItemPoolInterface` in your code.
Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-6-cache.md)
for details.
