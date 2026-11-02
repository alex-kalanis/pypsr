from ..message.interfaces import ServerRequestInterface, ResponseInterface


class RequestHandlerInterface:
    """
    Handles a server request and produces a response.

    An HTTP request handler process an HTTP request in order to produce an
    HTTP response.
    """

    def handle(self, request: ServerRequestInterface) -> ResponseInterface:
        """
        Handles a request and produces a response.

        May call other collaborating code to generate the response.

        Parameters
        ----------
        request: ServerRequestInterface

        Returns
        -------
        ResponseInterface
        """
        raise NotImplementedError('TBA')


class MiddlewareInterface:
    """
    Participant in processing a server request and response.

    An HTTP middleware component participates in processing an HTTP message:
    by acting on the request, generating the response, or forwarding the
    request to a subsequent middleware and possibly acting on its response.
    """

    def process(self, request: ServerRequestInterface, handler: RequestHandlerInterface) -> ResponseInterface:
        """
        Process an incoming server request.

        Processes an incoming server request in order to produce a response.
        If unable to produce the response itself, it may delegate to the provided
        request handler to do so.

        Parameters
        ----------
        request: ServerRequestInterface
        handler: RequestHandlerInterface

        Returns
        -------
        ResponseInterface
        """
        raise NotImplementedError('TBA')
