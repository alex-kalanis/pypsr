from typing import Any, Optional
from .enums import LogLevel
from .interfaces import LoggerInterface


class LoggerTrait(LoggerInterface):
    """
    This is a simple Logger trait that classes unable to extend AbstractLogger
    (because they extend another class, etc.) can include.

    It simply delegates all log-level-specific methods to the `log` method to
    reduce boilerplate code that a simple Logger that does the same thing with
    messages regardless of the error level has to implement.
    """

    def emergency(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        System is unusable.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.EMERGENCY, message, context)

    def alert(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Action must be taken immediately.

        Example: Entire website down, database unavailable, etc. This should
        trigger the SMS alerts and wake you up.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.ALERT, message, context)

    def critical(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Critical conditions.

        Example: Application component unavailable, unexpected exception.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.CRITICAL, message, context)

    def error(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Runtime errors that do not require immediate action but should typically
        be logged and monitored.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.ERROR, message, context)

    def warning(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Exceptional occurrences that are not errors.

        Example: Use of deprecated APIs, poor use of an API, undesirable things
        that are not necessarily wrong.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.WARNING, message, context)

    def notice(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Normal but significant events.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.NOTICE, message, context)

    def info(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Interesting events.

        Example: User logs in, SQL logs.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.INFO, message, context)

    def debug(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Detailed debug information.

        Args:
            message: The log message (string or object with __str__ method)
            context: Additional context information
        """
        if context is None:
            context = {}
        self.log(LogLevel.DEBUG, message, context)

    """
    Method "log" is not here because Python does not have real traits and allows multiple parent for classes
    """


class LoggerAwareTrait:
    """
    Basic Implementation of LoggerAwareInterface.
    """

    def __init__(self):
        self._logger: Optional[LoggerInterface] = None

    def set_logger(self, logger: LoggerInterface) -> None:
        """
        Sets a logger.

        Args:
            logger: A logger instance implementing the LoggerInterface
        """
        self._logger = logger
