from datetime import datetime
from .interfaces import ClockInterface


class CurrentDateTime(ClockInterface):
    """
    This class is used for access to current datetime on system
    """

    def now(self) -> datetime:
        return datetime.now()
