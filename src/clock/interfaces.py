from datetime import datetime


class ClockInterface:
    """
    Reimplementation of PHP PSR-20
    """

    def now(self) -> datetime:
        """
        Returns the current time as a datetime Object

        Returns
        -------
        datetime : datetime object
        """
        raise NotImplementedError('TBA')
