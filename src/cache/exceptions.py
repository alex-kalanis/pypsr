class CacheException(Exception):
    """
    Exception interface for all exceptions thrown by an Implementing Library.
    """
    pass


class InvalidArgumentException(CacheException):
    """
    Exception interface for invalid cache arguments.

    Any time an invalid argument is passed into a method it must throw an
    exception class which implements pypsr.cache.InvalidArgumentException.
    """
    pass
