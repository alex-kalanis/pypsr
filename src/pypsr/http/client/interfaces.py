from ..message.interfaces import RequestInterface, ResponseInterface


class ClientInterface:

    def send_request(self, request: RequestInterface) -> ResponseInterface:
        """
        Sends a PSR-7 request and returns a PSR-7 response.

        Parameters
        ----------
        request: RequestInterface

        Returns
        -------
        ResponseInterface

        Raises
        ------
        pypsr.http.client.ClientExceptionInterface
            If an error happens while processing the request.
        """
        raise NotImplementedError('TBA')
