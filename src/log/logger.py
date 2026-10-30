from typing import Any, Optional
from .enums import LogLevel
from .interfaces import LoggerInterface
from .traits import LoggerTrait


class EnumLevelsAdapter:
    """
    Operations with enum of level
    """

    @staticmethod
    def number_to_level(level: int) -> LogLevel:
        """
        Map error level number to LogLevel class

        When invalid level is set it returns level Error

        Parameters
        ----------
        level: int
            Log level

        Returns
        -------
        LogLevel
            Log level as Enum
        """
        inv_map = {v: k for k, v in LogLevel.get_num_map().items()}
        return inv_map.get(level, LogLevel.ERROR)

    @staticmethod
    def level_to_number(level: LogLevel) -> int:
        """
        Map log level class to number

        When invalid level is set it returns level 3 (Error)

        Parameters
        ----------
        level: LogLevel
            Log level class

        Returns
        -------
        int
            Log level as number
        """
        return LogLevel.get_num_map().get(level, 3)  # level error

    @staticmethod
    def short_to_level(level: str) -> LogLevel:
        """
        Map error level short string to LogLevel class

        When invalid level is set it returns level Error

        Parameters
        ----------
        level: str
            Log level

        Returns
        -------
        LogLevel
            Log level as Enum
        """
        inv_map = {v: k for k, v in LogLevel.get_short_map().items()}
        return inv_map.get(level, LogLevel.ERROR)

    @staticmethod
    def level_to_short(level: LogLevel) -> str:
        """
        Map log level class to short string

        When invalid level is set it returns level 3 (Error)

        Parameters
        ----------
        level: LogLevel
            Log level class

        Returns
        -------
        str
            Log level as shorten string
        """
        return LogLevel.get_short_map().get(level, 'err')  # level error


class AbstractLogger(LoggerInterface, LoggerTrait):
    """
    This is a simple Logger implementation that other Loggers can inherit from.

    It simply delegates all log-level-specific methods to the `log` method to
    reduce boilerplate code that a simple Logger that does the same thing with
    messages regardless of the error level has to implement.
    """
    pass


class NullLogger(AbstractLogger):
    """
    This Logger can be used to avoid conditional log calls.

    Logging should always be optional, and if no logger is provided to your
    library creating a NullLogger instance to have something to throw logs at
    is a good way to avoid littering your code with `if self.logger: ...`
    blocks.
    """

    def log(self, level: LogLevel | str | int, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Logs with an arbitrary level.

        Parameters
        ----------
        level: LogLevel | str | int
            The log level
        message: str
            The log message
        context: dict[str, Any] | None
            Additional context information (default: {})

        Returns
        -------
        None
        """
        # noop
        pass
