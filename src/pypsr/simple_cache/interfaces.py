from typing import Any
import datetime as dt


class CacheInterface:

    def get(self, key: str, default: Any | None = None) -> Any | None:
        """
        Fetches a value from the cache.

        Parameters
        ----------
        key: str
            The unique key of this item in the cache.
        default: Any | None
            Default value to return if the key does not exist.

        Returns
        -------
        Any | None
            The value of the item from the cache, or `default` in case of cache miss.

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if the `key` string is not a legal value.
        """
        raise NotImplementedError('TBA')

    def set(self, key: str, value: Any, ttl: int | dt.timedelta | None = None) -> bool:
        """
        Persists data in the cache, uniquely referenced by a key with an optional expiration TTL time.

        Parameters
        ----------
        key: str
            The key of the item to store.
        value: str
            The value of the item to store. Must be serializable.
        ttl: int | dt.timedelta | None
            Optional. The TTL value of this item. If no value is sent and
            the driver supports TTL then the library may set a default value
            for it or let the driver take care of that.

        Returns
        -------
        bool
            True on success and False on failure.

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if the `key` string is not a legal value.
        """
        raise NotImplementedError('TBA')

    def delete(self, key: str) -> bool:
        """
        Delete an item from the cache by its unique key.

        Parameters
        ----------
        key: str
            The unique cache key of the item to delete.

        Returns
        -------
        bool
            True if the item was successfully removed. False if there was an error.

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if the `key` string is not a legal value.
        """
        raise NotImplementedError('TBA')

    def clear(self) -> bool:
        """
        Wipes clean the entire cache's keys.

        Returns
        -------
        bool
            True on success and False on failure.
        """
        raise NotImplementedError('TBA')

    def get_multiple(self, keys: list[str], default: Any | None = None) -> dict[str, Any]:
        """
        Obtains multiple cache items by their unique keys.

        Parameters
        ----------
        keys: list[str]
            A list of keys that can obtained in a single operation.
        default: Any
            Default value to return for keys that do not exist.

        Returns
        -------
        dict[Any]
            A dictionary of key => value pairs. Cache keys that do not exist or are stale will have `default` as value.

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if the `keys` is neither a list of string keys nor a Traversable with string keys or
            if any of the `keys` are not a legal value.
        """
        raise NotImplementedError('TBA')

    def set_multiple(self, values: dict[str, Any], ttl: int | dt.timedelta | None = None) -> bool:
        """
        Persists a set of key => value pairs in the cache, with an optional TTL.

        Parameters
        ----------
        values: dict[str, Any]
            A dictionary of key => value pairs for a multiple-set operation.
        ttl: int | dt.timedelta | None
            Optional. The TTL value of this item. If no value is sent and
            the driver supports TTL then the library may set a default value
            for it or let the driver take care of that.

        Returns
        -------
        bool
            True on success and False on failure.

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if `values` is neither a list of serializable objects nor a Traversable
            with string keys or if any of the `keys` are not a legal value.
        """
        raise NotImplementedError('TBA')

    def delete_multiple(self, keys: list[str]) -> bool:
        """
        Deletes multiple cache items in a single operation.

        Parameters
        ----------
        keys: list[str]
            A list of string-based keys to be deleted.

        Returns
        -------
        bool
            True if the items were successfully removed. False if there was an error.

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if `keys` is not a list of strings
            or if any of the `keys` are not a legal value.
        """
        raise NotImplementedError('TBA')

    def has(self, key: str) -> bool:
        """
        Determines whether an item is present in the cache.

        NOTE: It is recommended that has() is only to be used for cache warming type purposes
        and not to be used within your live applications operations for get/set, as this method
        is subject to a race condition where your has() will return true and immediately after,
        another script can remove it, making the state of your app out of date.

        Parameters
        ----------
        key: str
            The cache item key.

        Returns
        -------
        bool

        Raises
        ------
        pypsr.simple_cache.exceptions.InvalidArgumentException
            MUST be thrown if the `key` string is not a legal value.
        """
        raise NotImplementedError('TBA')
