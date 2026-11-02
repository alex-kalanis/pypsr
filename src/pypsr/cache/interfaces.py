import datetime as dt


class CacheItemInterface:
    """
    CacheItemInterface defines an interface for interacting with objects inside a cache.
    """

    def get_key(self) -> str:
        """
        Returns the key for the current cache item.

        The key is loaded by the Implementing Library, but should be available to
        the higher level callers when needed.

        Returns
        -------
        str
            The key string for this cache item.
        """
        raise NotImplementedError('TBA')

    def get(self) -> object | None:
        """
        Retrieves the value of the item from the cache associated with this object's key.

        The value returned must be identical to the value originally stored by set().

        If is_hit() returns False, this method MUST return None. Note that None
        is a legitimate, cached value, so the is_hit() method SHOULD be used to
        differentiate between "None value was found" and "no value was found".

        Returns
        -------
        object or None
            The value corresponding to this cache item's key, or None if not found.
        """
        raise NotImplementedError('TBA')

    def is_hit(self) -> bool:
        """
        Confirms if the cache item lookup resulted in a cache hit.

        Note: This method MUST NOT have a race condition between calling is_hit()
        and calling get().

        Returns
        -------
        bool
            True if the request resulted in a cache hit. False otherwise.
        """
        raise NotImplementedError('TBA')

    def set(self, value: object) -> 'CacheItemInterface':
        """
        Sets the value represented by this cache item.

        The value argument may be any item that can be serialized by Python,
        although the method of serialization is left up to the Implementing
        Library.

        Parameters
        ----------
        value: object
            The serializable value to be stored.

        Returns
        -------
        CacheItemInterface
            The invoked object.
        """
        raise NotImplementedError('TBA')

    def expires_at(self, expiration: dt.datetime | None) -> 'CacheItemInterface':
        """
        Sets the expiration time for this cache item.

        Parameters
        ----------
        expiration: datetime.datetime | None
            The point in time after which the item MUST be considered expired.
            If None is passed explicitly, a default value MAY be used. If none is set,
            the value should be stored permanently or for as long as the
            implementation allows.

        Returns
        -------
        CacheItemInterface
            The called object.
        """
        raise NotImplementedError('TBA')

    def expires_after(self, time: int | dt.timedelta | None) -> 'CacheItemInterface':
        """
        Sets the expiration time for this cache item.

        Parameters
        ----------
        time: int | dt.timedelta | None
            The period of time from the present after which the item MUST be considered
            expired. An integer parameter is understood to be the time in seconds until
            expiration. If None is passed explicitly, a default value MAY be used.
            If none is set, the value should be stored permanently or for as long as the
            implementation allows.

        Returns
        -------
        CacheItemInterface
            The called object.
        """
        raise NotImplementedError('TBA')


class CacheItemPoolInterface:
    """
    CacheItemPoolInterface generates CacheItemInterface objects.
    """

    def get_item(self, key: str) -> CacheItemInterface:
        """
        Returns a Cache Item representing the specified key.

        This method must always return a CacheItemInterface object, even in case of
        a cache miss. It MUST NOT return None.

        Parameters
        ----------
        key: str
            The key for which to return the corresponding Cache Item.

        Returns
        -------
        CacheItemInterface
            The corresponding Cache Item.

        Raises
        ------
        pypsr.cache.exceptions.InvalidArgumentException
            If the key string is not a legal value a pypsr.cache.exceptions.InvalidArgumentException MUST be thrown.
        """
        raise NotImplementedError('TBA')

    def get_items(self, keys: list[str] | None = None) -> list[CacheItemInterface]:
        """
        Returns a traversable set of cache items.

        Parameters
        ----------
        keys: list of str or None
            An indexed array of keys of items to retrieve, None for all items.

        Returns
        -------
        list[CacheItemInterface]
            A traversable collection of Cache Items keyed by the cache keys of
            each item. A Cache item will be returned for each key, even if that
            key is not found. However, if no keys are specified then an empty
            traversable MUST be returned instead.

        Raises
        ------
        pypsr.cache.exceptions.InvalidArgumentException
            If any of the keys in keys are not a legal value a pypsr.cache.exceptions.InvalidArgumentException MUST be thrown.
        """
        raise NotImplementedError('TBA')

    def has_item(self, key: str) -> bool:
        """
        Confirms if the cache contains specified cache item.

        Note: This method MAY avoid retrieving the cached value for performance reasons.
        This could result in a race condition with CacheItemInterface::get(). To avoid
        such situation use CacheItemInterface::is_hit() instead.

        Parameters
        ----------
        key: str
            The key for which to check existence.

        Returns
        -------
        bool
            True if item exists in the cache, false otherwise.

        Raises
        ------
        pypsr.cache.exceptions.InvalidArgumentException
            If the key string is not a legal value a pypsr.cache.exceptions.InvalidArgumentException MUST be thrown.
        """
        raise NotImplementedError('TBA')

    def clear(self) -> bool:
        """
        Deletes all items in the pool.

        Returns
        -------
        bool
            True if the pool was successfully cleared. False if there was an error.
        """
        raise NotImplementedError('TBA')

    def delete_item(self, key: str) -> bool:
        """
        Removes the item from the pool.

        Parameters
        ----------
        key: str
            The key to delete.

        Returns
        -------
        bool
            True if the item was successfully removed. False if there was an error.

        Raises
        ------
        pypsr.cache.exceptions.InvalidArgumentException
            If the key string is not a legal value a pypsr.cache.exceptions.InvalidArgumentException MUST be thrown.
        """
        raise NotImplementedError('TBA')

    def delete_items(self, keys: list[str]) -> bool:
        """
        Removes multiple items from the pool.

        Parameters
        ----------
        keys: list[str]
            A list of keys that should be removed from the pool.

        Returns
        -------
        bool
            True if the items were successfully removed. False if there was an error.

        Raises
        ------
        pypsr.cache.exceptions.InvalidArgumentException
            If any of the keys in keys are not a legal value a pypsr.cache.exceptions.InvalidArgumentException MUST be thrown.
        """
        raise NotImplementedError('TBA')

    def save(self, item: CacheItemInterface) -> bool:
        """
        Persists a cache item immediately.

        Parameters
        ----------
        item: CacheItemInterface
            The cache item to save.

        Returns
        -------
        bool
            True if the item was successfully persisted. False if there was an error.
        """
        raise NotImplementedError('TBA')

    def save_deferred(self, item: CacheItemInterface) -> bool:
        """
        Sets a cache item to be persisted later.

        Parameters
        ----------
        item: CacheItemInterface
            The cache item to save.

        Returns
        -------
        bool
            False if the item could not be queued or if a commit was attempted and failed. True otherwise.
        """
        raise NotImplementedError('TBA')

    def commit(self) -> bool:
        """
        Persists any deferred cache items.

        Returns
        -------
        bool
            True if all not-yet-saved items were successfully saved or there were none. False otherwise.
        """
        raise NotImplementedError('TBA')
