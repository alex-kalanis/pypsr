PSR HTTP Client
===============

This directory holds all interfaces/classes/traits related to
[PSR-18](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-18-http-client.md).

Note that this is not an HTTP client of its own. It is merely an interface that
describes a client. See the specification for more details.

Installation
------------

With the rest of the package.

```bash
pip3 install pypsr
```

Usage
-----

If you need an http client, you can use the interface like this:

```python
from pypsr.http.client.interfaces import ClientInterface
from pypsr.http.client.exceptions import RequestExceptionInterface
from pypsr.http.message.interfaces import RequestInterface, RequestFactoryInterface, UriFactoryInterface


class RequestException(RequestExceptionInterface):

    def __init__(self, request: RequestInterface, *args: object):
        self._req: RequestInterface = request

    def get_request(self) -> RequestInterface:
        return self._req


class Foo:

    def __init__(
            self,
            http: ClientInterface,
            request_factory: RequestFactoryInterface,
            uri_factory: UriFactoryInterface,
    ):
        self._request: RequestFactoryInterface = request_factory
        self._uri: UriFactoryInterface = uri_factory
        self._http: ClientInterface = http

    def get_something_from_remote(self) -> str:
        request = self._request.create_request(
            'GET',
            self._uri.create_uri('http://example.com:99999/foo-bar')
        )
        response = self._http.send_request(request)
        if 200 != response.get_status_code():
            raise RequestException(request)
        return response.get_body().value().decode('utf-8')

    # do something else useful
```

You can then pick one of the implementations of the interface to get a container.

If you want to implement the interface, you can require this package and
implement `pypsr.http.client.interfaces.ClientInterface` in your code.
Please read the
[specification text](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-18-http-client.md)
for details.
