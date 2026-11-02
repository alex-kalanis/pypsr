
class CacheException(Exception):
    """
    Interface used for all types of exceptions thrown by the implementing library.
    """
    pass


class InvalidArgumentException(CacheException):
    """
    Exception interface for invalid cache arguments.

    When an invalid argument is passed, it must throw an exception which implements
    this interface.
    """
    pass
