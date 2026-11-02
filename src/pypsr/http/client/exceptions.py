from ..message.interfaces import RequestInterface


class ClientExceptionInterface(Exception):
    """
    Every HTTP client related exception MUST implement this interface.
    """
    pass


class RequestExceptionInterface(ClientExceptionInterface):
    """
    Exception for when a request failed.

    Examples:
      - Request is invalid (e.g. method is missing)
      - Runtime request errors (e.g. the body stream is not seekable)
    """

    def get_request(self) -> RequestInterface:
        """
        Returns the request.

        The request object MAY be a different object from the one passed to ClientInterface.send_request()

        Returns
        -------
        RequestInterface
        """
        raise NotImplementedError('TBA')


class NetworkExceptionInterface(ClientExceptionInterface):
    """
    Thrown when the request cannot be completed because of network issues.

    There is no response object as this exception is thrown when no response has been received.

    Example: the target host name can not be resolved or the connection failed.
    """

    def get_request(self) -> RequestInterface:
        """
        Returns the request.

        The request object MAY be a different object from the one passed to ClientInterface.send_request()

        Returns
        -------
        RequestInterface
        """
        raise NotImplementedError('TBA')
