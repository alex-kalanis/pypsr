from enum import Enum


class LogLevel(str, Enum):
    """
    Describes log levels.
    @link https://signoz.io/guides/syslog-levels/
    @link https://www.solarwinds.com/resources/it-glossary/syslog-levels
    @link https://resources.cloudcops.com/blogs/syslog-severity-levels
    """

    EMERGENCY = 'emergency'
    ALERT = 'alert'
    CRITICAL = 'critical'
    ERROR = 'error'
    WARNING = 'warning'
    NOTICE = 'notice'
    INFO = 'info'
    DEBUG = 'debug'

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def get_num_map() -> dict['LogLevel', int]:
        """
        Get map of log levels.

        Returns
        -------
        dict[LogLevel, int]
            Map of log levels - from class to int
        """
        return {
            LogLevel.EMERGENCY: 0,
            LogLevel.ALERT: 1,
            LogLevel.CRITICAL: 2,
            LogLevel.ERROR: 3,
            LogLevel.WARNING: 4,
            LogLevel.NOTICE: 5,
            LogLevel.INFO: 6,
            LogLevel.DEBUG: 7,
        }

    @staticmethod
    def get_short_map() -> dict['LogLevel', str]:
        """
        Get map of log levels.

        Returns
        -------
        dict[LogLevel, str]
            Map of log levels - from class to shorten string
        """
        return {
            LogLevel.EMERGENCY: 'emerg',
            LogLevel.ALERT: 'alert',
            LogLevel.CRITICAL: 'crit',
            LogLevel.ERROR: 'err',
            LogLevel.WARNING: 'warning',
            LogLevel.NOTICE: 'notice',
            LogLevel.INFO: 'info',
            LogLevel.DEBUG: 'debug',
        }
