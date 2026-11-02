from typing import TypeVar, Callable, Iterable

TD = TypeVar('TD')  # Type of dispatching Class


class EventDispatcherInterface:
    """
    Defines a dispatcher for events.
    """

    def dispatch(self, event: TD) -> TD:
        """
        Provide all relevant listeners with an event to process.

        Parameters
        ----------
        event: TD
            The object to process.

        Returns
        -------
        TD
            The Event that was passed, now modified by listeners.
        """
        raise NotImplementedError('TBA')


class ListenerProviderInterface:
    """
    Mapper from an event to the listeners that are applicable to that event.
    """

    def get_listeners_for_event(self, event: TD) -> Iterable[Callable[[TD], TD]]:
        """

        Parameters
        ----------
        event: TD
            An event for which to return the relevant listeners.

        Returns
        -------
        Iterable[Callable[[TD], TD]]
            An iterable (list, tuple or generator) of callables. Each
            callable MUST be type-compatible with `event`.
        """
        raise NotImplementedError('TBA')


class StoppableEventInterface:
    """
    An Event whose processing may be interrupted when the event has been handled.

    A Dispatcher implementation MUST check to determine if an Event
    is marked as stopped after each listener is called.  If it is then it should
    return immediately without calling any further Listeners.
    """

    def is_propagation_stopped(self) -> bool:
        """
        Is propagation stopped?

        This will typically only be used by the Dispatcher to determine if the
        previous listener halted propagation.

        Returns
        -------
        bool
            True if the Event is complete and no further listeners should be called.
            False to continue calling listeners.
        """
        raise NotImplementedError('TBA')
