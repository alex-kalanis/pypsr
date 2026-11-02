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

        Parameters
        ----------
        message: str
            The log message (string or object with __str__ method)
        context: Optional[dict[str, Any]
            Additional context information

        Returns
        -------
        None
        """
        if context is None:
            context = {}
        self.log(LogLevel.EMERGENCY, message, context)

    def alert(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Action must be taken immediately.

        Example: Entire website down, database unavailable, etc. This should
        trigger the SMS alerts and wake you up.

        Parameters
        ----------
        message: str
            The log message (string or object with __str__ method)
        context: Optional[dict[str, Any]
            Additional context information

        Returns
        -------
        None
        """
        if context is None:
            context = {}
        self.log(LogLevel.ALERT, message, context)

    def critical(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Critical conditions.

        Example: Application component unavailable, unexpected exception.

        Parameters
        ----------
        message: str
            The log message
        context: dict[str, Any] or None
            Additional context information (default: None)
        """
        if context is None:
            context = {}
        self.log(LogLevel.CRITICAL, message, context)

    def error(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Runtime errors that do not require immediate action but should typically
        be logged and monitored.

        Parameters
        ----------
        message: str
            The log message
        context: dict[str, Any] or None
            Additional context information (default: None)
        """
        if context is None:
            context = {}
        self.log(LogLevel.ERROR, message, context)

    def warning(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Exceptional occurrences that are not errors.

        Example: Use of deprecated APIs, poor use of an API, undesirable things
        that are not necessarily wrong.

        Parameters
        ----------
        message: str
            The log message
        context: dict[str, Any] or None
            Additional context information (default: None)
        """
        if context is None:
            context = {}
        self.log(LogLevel.WARNING, message, context)

    def notice(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Normal but significant events.

        Parameters
        ----------
        message: str
            The log message
        context: dict[str, Any] or None
            Additional context information (default: None)
        """
        if context is None:
            context = {}
        self.log(LogLevel.NOTICE, message, context)

    def info(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Interesting events.

        Example: User logs in, SQL logs.

        Parameters
        ----------
        message: str
            The log message
        context: dict[str, Any] or None
            Additional context information (default: None)
        """
        if context is None:
            context = {}
        self.log(LogLevel.INFO, message, context)

    def debug(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Detailed debug information.

        Parameters
        ----------
        message: str
            The log message
        context: dict[str, Any] or None
            Additional context information (default: None)
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
        Sets a logger instance on the object.

        Parameters
        ----------
        logger: LoggerInterface
        """
        self._logger = logger
