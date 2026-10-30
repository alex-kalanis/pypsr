from typing import Any, Optional
from .enums import LogLevel
from .interfaces import LoggerInterface
from .traits import LoggerTrait


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

        Args:
            level: The log level
            message: The log message
            context: Additional context information (default: {})
        """

        # noop
        pass
