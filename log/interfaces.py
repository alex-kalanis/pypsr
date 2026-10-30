from typing import Any, Optional
from .enums import LogLevel


class LoggerInterface:
    """
    Describes a logger instance.
    This one is copied from PHP PSR-3 and that is based on RFC 5424 and Syslog

    The message MUST be a string or object implementing __str__().

    The message MAY contain placeholders in the form: {foo} where foo
    will be replaced by the context data in key "foo".

    The context dictionary can contain arbitrary data, the only assumption that
    can be made by implementors is that if an Exception instance is given
    to produce a stack trace, it MUST be in a key named "exception".

    See https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md
    for the full interface specification.
    """

    def emergency(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        System is unusable.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def alert(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Action must be taken immediately.

        Example: Entire website down, database unavailable, etc. This should
        trigger the SMS alerts and wake you up.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def critical(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Critical conditions.

        Example: Application component unavailable, unexpected exception.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def error(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Runtime errors that do not require immediate action but should typically
        be logged and monitored.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def warning(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Exceptional occurrences that are not errors.

        Example: Use of deprecated APIs, poor use of an API, undesirable things
        that are not necessarily wrong.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def notice(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Normal but significant events.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def info(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Interesting events.

        Example: User logs in, SQL logs.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def debug(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Detailed debug information.

        Args:
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')

    def log(self, level: LogLevel | str | int, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Logs with an arbitrary level.

        Args:
            level: The log level
            message: The log message
            context: Additional context information (default: {})
        """
        raise NotImplementedError('TBA')


class LoggerAwareInterface:
    """
     Describes a logger-aware instance.
    """

    def set_logger(self, logger: LoggerInterface) -> None:
        """
        Sets a logger instance on the object.

        Parameters
        ----------
        logger

        Returns
        -------

        """
        raise NotImplementedError('TBA')
