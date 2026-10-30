from enum import Enum


class LogLevel(str, Enum):
    """
    Describes log levels.
    @link https://signoz.io/guides/syslog-levels/
    @link https://www.solarwinds.com/resources/it-glossary/syslog-levels
    @link https://resources.cloudcops.com/blogs/syslog-severity-levels
    """

    EMERGENCY = 'emerg'
    ALERT = 'alert'
    CRITICAL = 'crit'
    ERROR = 'err'
    WARNING = 'warning'
    NOTICE = 'notice'
    INFO = 'info'
    DEBUG = 'debug'

    def __str__(self) -> str:
        return str(self.value)
