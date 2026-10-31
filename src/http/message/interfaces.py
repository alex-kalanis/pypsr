from io import BytesIO
from typing import Any


class UriInterface:
    """
    Value object representing a URI.

    This interface is meant to represent URIs according to RFC 3986 and to
    provide methods for most common operations. Additional functionality for
    working with URIs can be provided on top of the interface or externally.
    Its primary use is for HTTP requests, but may also be used in other
    contexts.

    Instances of this interface are considered immutable; all methods that
    might change state MUST be implemented such that they retain the internal
    state of the current instance and return an instance that contains the
    changed state.

    Typically the Host header will be also be present in the request message.
    For server-side requests, the scheme will typically be discoverable in the
    server parameters.

    * @link https://tools.ietf.org/html/rfc3986 (the URI specification)
    """

    def get_scheme(self) -> str:
        """
        Retrieve the scheme component of the URI.

        If no scheme is present, this method MUST return an empty string.

        The value returned MUST be normalized to lowercase, per RFC 3986
        Section 3.1.

        The trailing ":" character is not part of the scheme and MUST NOT be
        added.

        * @see https://tools.ietf.org/html/rfc3986#section-3.1

        Returns
        -------
        str
            The URI scheme.
        """
        raise NotImplementedError('TBA')

    def get_authority(self) -> str:
        """
        Retrieve the authority component of the URI.

        If no authority information is present, this method MUST return an empty
        string.

        The authority syntax of the URI is:

        ```<pre>
        [user-info@]host[:port]
        </pre>```

        If the port component is not set or is the standard port for the current
        scheme, it SHOULD NOT be included.

        * @see https://tools.ietf.org/html/rfc3986#section-3.2

        Returns
        -------
        str
            The URI authority, in "[user-info@]host[:port]" format.
        """
        raise NotImplementedError('TBA')

    def get_user_info(self) -> str:
        """
        Retrieve the user information component of the URI.

        If no user information is present, this method MUST return an empty
        string.

        If a user is present in the URI, this will return that value;
        additionally, if the password is also present, it will be appended to the
        user value, with a colon (":") separating the values.

        The trailing "@" character is not part of the user information and MUST
        NOT be added.

        Returns
        -------
        str
            The URI user information, in "username[:password]" format.
        """
        raise NotImplementedError('TBA')

    def get_host(self) -> str:
        """
        Retrieve the host component of the URI.

        If no host is present, this method MUST return an empty string.

        The value returned MUST be normalized to lowercase, per RFC 3986
        Section 3.2.2.

        * @see https://tools.ietf.org/html/rfc3986#section-3.2.2

        Returns
        -------
        str
            The URI host.
        """
        raise NotImplementedError('TBA')

    def get_port(self) -> int | None:
        """
        Retrieve the port component of the URI.

        If a port is present, and it is non-standard for the current scheme,
        this method MUST return it as an integer. If the port is the standard port
        used with the current scheme, this method SHOULD return None.

        If no port is present, and no scheme is present, this method MUST return
        a None value.

        If no port is present, but a scheme is present, this method MAY return
        the standard port for that scheme, but SHOULD return None.

        Returns
        -------
        int | None
            The URI port.
        """
        raise NotImplementedError('TBA')

    def get_path(self) -> str:
        """
        Retrieve the path component of the URI.

        The path can either be empty or absolute (starting with a slash) or
        rootless (not starting with a slash). Implementations MUST support all
        three syntaxes.

        Normally, the empty path "" and absolute path "/" are considered equal as
        defined in RFC 7230 Section 2.7.3. But this method MUST NOT automatically
        do this normalization because in contexts with a trimmed base path, e.g.
        the front controller, this difference becomes significant. It's the task
        of the user to handle both "" and "/".

        The value returned MUST be percent-encoded, but MUST NOT double-encode
        any characters. To determine what characters to encode, please refer to
        RFC 3986, Sections 2 and 3.3.

        As an example, if the value should include a slash ("/") not intended as
        delimiter between path segments, that value MUST be passed in encoded
        form (e.g., "%2F") to the instance.

         * @see https://tools.ietf.org/html/rfc3986#section-2
         * @see https://tools.ietf.org/html/rfc3986#section-3.3

        Returns
        -------
        str
            The URI path.
        """
        raise NotImplementedError('TBA')

    def get_query(self) -> str:
        """
        Retrieve the query string of the URI.

        If no query string is present, this method MUST return an empty string.

        The leading "?" character is not part of the query and MUST NOT be
        added.

        The value returned MUST be percent-encoded, but MUST NOT double-encode
        any characters. To determine what characters to encode, please refer to
        RFC 3986, Sections 2 and 3.4.

        As an example, if a value in a key/value pair of the query string should
        include an ampersand ("&") not intended as a delimiter between values,
        that value MUST be passed in encoded form (e.g., "%26") to the instance.

         * @see https://tools.ietf.org/html/rfc3986#section-2
         * @see https://tools.ietf.org/html/rfc3986#section-3.4

        Returns
        -------
        string
            The URI query string.
        """
        raise NotImplementedError('TBA')

    def get_fragment(self) -> str:
        """
        Retrieve the fragment component of the URI.

        If no fragment is present, this method MUST return an empty string.

        The leading "#" character is not part of the fragment and MUST NOT be
        added.

        The value returned MUST be percent-encoded, but MUST NOT double-encode
        any characters. To determine what characters to encode, please refer to
        RFC 3986, Sections 2 and 3.5.

         * @see https://tools.ietf.org/html/rfc3986#section-2
         * @see https://tools.ietf.org/html/rfc3986#section-3.5

        Returns
        -------
        string
            The URI fragment.
        """
        raise NotImplementedError('TBA')

    def with_scheme(self, scheme: str) -> 'UriInterface':
        """
        Return an instance with the specified scheme.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified scheme.

        Implementations MUST support the schemes "http" and "https" case
        insensitively, and MAY accommodate other schemes if required.

        An empty scheme is equivalent to removing the scheme.

        Parameters
        ----------
        scheme: str
            The scheme to use with the new instance.

        Returns
        -------
        UriInterface
            A new instance with the specified scheme.

        Raises
        ------
        AttributeError
            for invalid or unsupported schemes.
        """
        raise NotImplementedError('TBA')

    def with_user_info(self, user: str, password: str | None = None) -> 'UriInterface':
        """
        Return an instance with the specified user information.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified user information.

        Password is optional, but the user information MUST include the
        user; an empty string for the user is equivalent to removing user
        information.

        Parameters
        ----------
        user: str
            The user name to use for authority.
        password: str | None
            The password associated with user.

        Returns
        -------
        UriInterface
            A new instance with the specified user information.
        """
        raise NotImplementedError('TBA')

    def with_host(self, host: str) -> 'UriInterface':
        """
        Return an instance with the specified host.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified host.

        An empty host value is equivalent to removing the host.

        Parameters
        ----------
        host: string
            The hostname to use with the new instance.

        Returns
        -------
        UriInterface
            A new instance with the specified host.

        Raises
        ------
        AttributeError
            for invalid hostnames.
        """
        raise NotImplementedError('TBA')

    def with_port(self, port: int | None) -> 'UriInterface':
        """
        Return an instance with the specified port.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified port.

        Implementations MUST raise an exception for ports outside the
        established TCP and UDP port ranges.

        A null value provided for the port is equivalent to removing the port
        information.

        Parameters
        ----------
        port: int | None
            The port to use with the new instance; a None value removes the port information.

        Returns
        -------
        UriInterface
            A new instance with the specified port.

        Raises
        ------
        AttributeError
            for invalid ports.
        """
        raise NotImplementedError('TBA')

    def with_path(self, path: str) -> 'UriInterface':
        """
        Return an instance with the specified path.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified path.

        The path can either be empty or absolute (starting with a slash) or
        rootless (not starting with a slash). Implementations MUST support all
        three syntaxes.

        If the path is intended to be domain-relative rather than path relative then
        it must begin with a slash ("/"). Paths not starting with a slash ("/")
        are assumed to be relative to some base path known to the application or
        consumer.

        Users can provide both encoded and decoded path characters.
        Implementations ensure the correct encoding as outlined in get_path().

        Parameters
        ----------
        path: str
            The path to use with the new instance.

        Returns
        -------
        UriInterface
            A new instance with the specified path.

        Raises
        ------
        AttributeError
            for invalid paths.
        """
        raise NotImplementedError('TBA')

    def with_query(self, query: str) -> 'UriInterface':
        """
        Return an instance with the specified query string.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified query string.

        Users can provide both encoded and decoded query characters.
        Implementations ensure the correct encoding as outlined in get_query().

        An empty query string value is equivalent to removing the query string.

        Parameters
        ----------
        query: str
            The query string to use with the new instance.

        Returns
        -------
        UriInterface
            A new instance with the specified query string.

        Raises
        ------
        AttributeError
            for invalid query strings.
        """
        raise NotImplementedError('TBA')

    def with_fragment(self, fragment: str) -> 'UriInterface':
        """
        Return an instance with the specified URI fragment.

        This method MUST retain the state of the current instance, and return
        an instance that contains the specified URI fragment.

        Users can provide both encoded and decoded fragment characters.
        Implementations ensure the correct encoding as outlined in getFragment().

        An empty fragment value is equivalent to removing the fragment.

        Parameters
        ----------
        fragment: str
            The fragment to use with the new instance.

        Returns
        -------
        UriInterface
            A new instance with the specified fragment.
        """
        raise NotImplementedError('TBA')

    def __str__(self) -> str:
        """
        Return the string representation as a URI reference.

        Depending on which components of the URI are present, the resulting
        string is either a full URI or relative reference according to RFC 3986,
        Section 4.1. The method concatenates the various components of the URI,
        using the appropriate delimiters:

         - If a scheme is present, it MUST be suffixed by ":".
         - If an authority is present, it MUST be prefixed by "//".
         - The path can be concatenated without delimiters. But there are two
           cases where the path has to be adjusted to make the URI reference
           valid as Python does not want to raise an exception in __str__():
             - If the path is rootless and an authority is present, the path MUST
               be prefixed by "/".
             - If the path is starting with more than one "/" and no authority is
               present, the starting slashes MUST be reduced to one.
         - If a query is present, it MUST be prefixed by "?".
         - If a fragment is present, it MUST be prefixed by "#".

         * @see https://tools.ietf.org/html/rfc3986#section-4.1

        Returns
        -------
        string
        """
        raise NotImplementedError('TBA')


class UploadedFileInterface:
    """
    Value object representing a file uploaded through an HTTP request.

    Instances of this interface are considered immutable; all methods that
    might change state MUST be implemented such that they retain the internal
    state of the current instance and return an instance that contains the
    changed state.
    """

    def get_stream(self) -> BytesIO:
        """
        Retrieve a stream representing the uploaded file.

        This method MUST return a BytesIO instance, representing the
        uploaded file. The purpose of this method is to allow utilizing native Python
        stream functionality to manipulate the file upload, such as
        `with X:` construct.

        If the move_to() method has been called previously, this method MUST raise
        an exception.

        Returns
        -------
        BytesIO
            Stream representation of the uploaded file.

        Raises
        ------
        RuntimeError
            in cases when no stream is available or can be created.
        """
        raise NotImplementedError('TBA')

    def move_to(self, target_path: str) -> None:
        """
        Move the uploaded file to a new location.

        Use this method as an alternative to move_uploaded_file(). This method is
        guaranteed to work in both SAPI and non-SAPI environments.
        Implementations must determine which environment they are in, and use the
        appropriate method (move_uploaded_file(), rename(), or a stream
        operation) to perform the operation.

        `target_path` may be an absolute path, or a relative path. If it is a
        relative path, resolution should be the same as used by PHP's rename()
        function.

        The original file or stream MUST be removed on completion.

        If this method is called more than once, any subsequent calls MUST raise
        an exception.

        When used in an SAPI environment where _FILES is populated, when writing
        files via move_to(), is_uploaded_file() and move_uploaded_file() SHOULD be
        used to ensure permissions and upload status are verified correctly.

        If you wish to move to a stream, use get_stream(), as SAPI operations
        cannot guarantee writing to stream destinations.

         * @see https://php.net/is_uploaded_file
         * @see https://php.net/move_uploaded_file

        Parameters
        ----------
        target_path: str
            Path to which to move the uploaded file.

        Raises
        ------
        AttributeError
            if the target_path specified is invalid.
        RuntimeError
            on any error during the move operation, or on the second or subsequent call to the method.
        """
        raise NotImplementedError('TBA')

    def get_size(self) -> int | None:
        """
        Retrieve the file size.

        Implementations SHOULD return the value stored in the "size" key of
        the file in the _FILES array if available, as PHP calculates this based
        on the actual size transmitted.

        Returns
        -------
        int | None
            The file size in bytes or None if unknown.
        """
        raise NotImplementedError('TBA')

    def get_error(self) -> int:
        """
        Retrieve the error associated with the uploaded file.

        The return value MUST be one of PHP's UPLOAD_ERR_XXX constants.

        If the file was uploaded successfully, this method MUST return
        UPLOAD_ERR_OK.

        Implementations SHOULD return the value stored in the "error" key of
        the file in the _FILES array.

        * @see https://php.net/manual/en/features.file-upload.errors.php

        Returns
        -------
        int
            One of PHP's UPLOAD_ERR_XXX constants.
        """
        raise NotImplementedError('TBA')

    def get_client_filename(self) -> str | None:
        """
        Retrieve the filename sent by the client.

        Do not trust the value returned by this method. A client could send
        a malicious filename with the intention to corrupt or hack your
        application.

        Implementations SHOULD return the value stored in the "name" key of
        the file in the _FILES array.

        Returns
        -------
        string | None
            The filename sent by the client or null if none was provided.
        """
        raise NotImplementedError('TBA')

    def get_client_media_type(self) -> str | None:
        """
        Retrieve the media type sent by the client.

        Do not trust the value returned by this method. A client could send
        a malicious media type with the intention to corrupt or hack your
        application.

        Implementations SHOULD return the value stored in the "type" key of
        the file in the _FILES array.

        Returns
        -------
        string|None
            The media type sent by the client or null if none was provided.
        """
        raise NotImplementedError('TBA')


class MessageInterface:
    """
    HTTP messages consist of requests from a client to a server and responses
    from a server to a client. This interface defines the methods common to
    each.

    Messages are considered immutable; all methods that might change state MUST
    be implemented such that they retain the internal state of the current
    message and return an instance that contains the changed state.

    @link https://www.ietf.org/rfc/rfc7230.txt
    @link https://www.ietf.org/rfc/rfc7231.txt
    """

    def get_protocol_version(self) -> str:
        """
        Retrieves the HTTP protocol version as a string.

        The string MUST contain only the HTTP version number (e.g., "1.1", "1.0").

        Returns
        -------
        str
            HTTP protocol version.
        """
        raise NotImplementedError('TBA')

    def with_protocol_version(self, version: str) -> 'MessageInterface':
        """
        Return an instance with the specified HTTP protocol version.

        The version string MUST contain only the HTTP version number (e.g.,
        "1.1", "1.0").

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        new protocol version.

        Parameters
        ----------
        version: str
            HTTP protocol version

        Returns
        -------
        MessageInterface
        """
        raise NotImplementedError('TBA')

    def get_headers(self) -> dict[str, list[str]]:
        """
        Retrieves all message header values.

        The keys represent the header name as it will be sent over the wire, and
        each value is an array of strings associated with the header.

        Examples
        --------
        >>> # Represent the headers as a string
        ... message = MessageInterface()
        ... for name, values in message.get_headers().items():
        ...    print(name + ": " + ", ".join(values))

        >>> # Emit headers iteratively
        ... message = MessageInterface()
        ... for name, values in message.get_headers().items():
        ...     for value in values:
        ...         print(f'{name}: {value}')

        While header names are not case-sensitive, get_headers() will preserve the
        exact case in which headers were originally specified.

        Returns
        -------
        dict[str, list[str]]
            Returns a list of the message's headers. Each key MUST be a header name,
            and each value MUST be a list of strings for that header.
        """
        raise NotImplementedError('TBA')

    def has_header(self, name: str) -> bool:
        """
        Checks if a header exists by the given case-insensitive name.

        Parameters
        ----------
        name: str
            Case-insensitive header field name.

        Returns
        -------
        bool
            Returns True if any header names match the given header
            name using a case-insensitive string comparison. Returns False if
            no matching header name is found in the message.
        """
        raise NotImplementedError('TBA')

    def get_header(self, name: str) -> list[str]:
        """
        Retrieves a message header value by the given case-insensitive name.

        This method returns an array of all the header values of the given
        case-insensitive header name.

        If the header does not appear in the message, this method MUST return an
        empty array.

        Parameters
        ----------
        name: str
            Case-insensitive header field name.

        Returns
        -------
        list[str]
            A list of string values as provided for the given
            header. If the header does not appear in the message, this method MUST
            return an empty list.
        """
        raise NotImplementedError('TBA')

    def get_header_line(self, name: str) -> str:
        """
        Retrieves a comma-separated string of the values for a single header.

        This method returns all of the header values of the given
        case-insensitive header name as a string concatenated together using
        a comma.

        NOTE: Not all header values may be appropriately represented using
        comma concatenation. For such headers, use get_header() instead
        and supply your own delimiter when concatenating.

        If the header does not appear in the message, this method MUST return
        an empty string.

        Parameters
        ----------
        name: str
            Case-insensitive header field name.

        Returns
        -------
        string
            A string of values as provided for the given header
            concatenated together using a comma. If the header does not appear in
            the message, this method MUST return an empty string.
        """
        raise NotImplementedError('TBA')

    def with_header(self, name: str, value: str | list[str]) -> 'MessageInterface':
        """
        Return an instance with the provided value replacing the specified header.

        While header names are case-insensitive, the casing of the header will
        be preserved by this function, and returned from getHeaders().

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        new and/or updated header and value.

        Parameters
        ----------
        name: str
            Case-insensitive header field name.
        value: str | list[str]
            Header value(s).

        Returns
        -------
        MessageInterface

        Raises
        ------
        AttributeError
            for invalid header names or values.
        """
        raise NotImplementedError('TBA')

    def with_added_header(self, name: str, value: str | list[str]) -> 'MessageInterface':
        """
        Return an instance with the specified header appended with the given value.

        Existing values for the specified header will be maintained. The new
        value(s) will be appended to the existing list. If the header did not
        exist previously, it will be added.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        new header and/or value.

        Parameters
        ----------
        name: str
            Case-insensitive header field name to add.
        value: str | list[str]
            Header value(s).

        Returns
        -------
        MessageInterface

        Raises
        ------
        AttributeError
            for invalid header names or values.
        """
        raise NotImplementedError('TBA')

    def without_header(self, name: str) -> 'MessageInterface':
        """
        Return an instance without the specified header.

        Header resolution MUST be done without case-sensitivity.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that removes
        the named header.

        Parameters
        ----------
        name: str
            Case-insensitive header field name to remove.

        Returns
        -------
        MessageInterface
        """
        raise NotImplementedError('TBA')

    def get_body(self) -> BytesIO:
        """
        Gets the body of the message.

        Returns
        -------
        bytes
            Returns the body as a stream of bytes.
        """
        raise NotImplementedError('TBA')

    def with_body(self, body: BytesIO) -> 'MessageInterface':
        """
        Return an instance with the specified message body.

        The body MUST be a BytesIO object.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return a new instance that has the
        new body stream.

        Parameters
        ----------
        body: BytesIO
            Body.

        Returns
        -------
        MessageInterface

        Raises
        ------
        AttributeError
            When the body is not valid.
        """
        raise NotImplementedError('TBA')


class RequestInterface(MessageInterface):
    """
    Representation of an outgoing, client-side request.

    Per the HTTP specification, this interface includes properties for
    each of the following:

    - Protocol version
    - HTTP method
    - URI
    - Headers
    - Message body

    During construction, implementations MUST attempt to set the Host header from
    a provided URI if no Host header is provided.

    Requests are considered immutable; all methods that might change state MUST
    be implemented such that they retain the internal state of the current
    message and return an instance that contains the changed state.
    """

    def get_request_target(self) -> str:
        """
        Retrieves the message's request target.

        Retrieves the message's request-target either as it will appear (for
        clients), as it appeared at request (for servers), or as it was
        specified for the instance (see with_request_target()).

        In most cases, this will be the origin-form of the composed URI,
        unless a value was provided to the concrete implementation (see
        with_request_target() below).

        If no URI is available, and no request-target has been specifically
        provided, this method MUST return the string "/".

        Returns
        -------
        str
        """
        raise NotImplementedError('TBA')

    def with_request_target(self, request_target: str) -> 'RequestInterface':
        """
        Return an instance with the specific request-target.

        If the request needs a non-origin-form request-target — e.g., for
        specifying an absolute-form, authority-form, or asterisk-form —
        this method may be used to create an instance with the specified
        request-target, verbatim.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        changed request target.

        * @link https://tools.ietf.org/html/rfc7230#section-5.3 (for the various
          request-target forms allowed in request messages)

        Parameters
        ----------
        request_target: string

        Returns
        -------
        RequestInterface
        """
        raise NotImplementedError('TBA')

    def get_method(self) -> str:
        """
        Retrieves the HTTP method of the request.

        Returns
        -------
        string
            Returns the request method.
        """
        raise NotImplementedError('TBA')

    def with_method(self, method: str) -> 'RequestInterface':
        """
        Return an instance with the provided HTTP method.

        While HTTP method names are typically all uppercase characters, HTTP
        method names are case-sensitive and thus implementations SHOULD NOT
        modify the given string.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        changed request method.

        Parameters
        ----------
        method: str
            Case-sensitive method.

        Returns
        -------
        RequestInterface

        Raises
        ------
        AttributeError
            for invalid HTTP methods.
        """
        raise NotImplementedError('TBA')

    def get_uri(self) -> UriInterface:
        """
        Retrieves the URI instance.

        This method MUST return a UriInterface instance.

        * @link https://tools.ietf.org/html/rfc3986#section-4.3

        Returns
        -------
        UriInterface
            Returns a UriInterface instance representing the URI of the request.
        """
        raise NotImplementedError('TBA')

    def with_uri(self, uri: UriInterface, preserve_host: bool = False) -> 'RequestInterface':
        """
        Returns an instance with the provided URI.

        This method MUST update the Host header of the returned request by
        default if the URI contains a host component. If the URI does not
        contain a host component, any pre-existing Host header MUST be carried
        over to the returned request.

        You can opt-in to preserving the original state of the Host header by
        setting `preserve_host` to `True`. When `preserve_host` is set to
        `True`, this method interacts with the Host header in the following ways:

        - If the Host header is missing or empty, and the new URI contains
          a host component, this method MUST update the Host header in the returned
          request.
        - If the Host header is missing or empty, and the new URI does not contain a
          host component, this method MUST NOT update the Host header in the returned
          request.
        - If a Host header is present and non-empty, this method MUST NOT update
          the Host header in the returned request.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        new UriInterface instance.

         * @link https://tools.ietf.org/html/rfc3986#section-4.3

        Parameters
        ----------
        uri: UriInterface
            New request URI to use.
        preserve_host: bool
            Preserve the original state of the Host header.

        Returns
        -------
        RequestInterface
        """
        raise NotImplementedError('TBA')


class ServerRequestInterface(RequestInterface):
    """
    Representation of an incoming, server-side HTTP request.

    Per the HTTP specification, this interface includes properties for
    each of the following:

    - Protocol version
    - HTTP method
    - URI
    - Headers
    - Message body

    Additionally, it encapsulates all data as it has arrived at the
    application from the CGI and/or Python environment, including:

    - The values represented in args.
    - Any cookies provided
    - Query string arguments
    - Upload files, if any
    - Deserialized body parameters

    SERVER values MUST be treated as immutable, as they represent application
    state at the time of request; as such, no methods are provided to allow
    modification of those values. The other values provide such methods, as they
    can be restored from SERVER or the request body, and may need treatment
    during the application (e.g., body parameters may be deserialized based on
    content type).

    Additionally, this interface recognizes the utility of introspecting a
    request to derive and match additional parameters (e.g., via URI path
    matching, decrypting cookie values, deserializing non-form-encoded body
    content, matching authorization headers to users, etc). These parameters
    are stored in an "attributes" property.

    Requests are considered immutable; all methods that might change state MUST
    be implemented such that they retain the internal state of the current
    message and return an instance that contains the changed state.
    """

    def get_server_params(self) -> dict[str, str | int | bool]:
        """
        Retrieve server parameters.

        Retrieves data related to the incoming request environment,
        typically derived from PHP's _SERVER superglobal. The data IS NOT
        REQUIRED to originate from _SERVER.

        Returns
        -------
        dict[str, str | int | bool]
            Dictionary of server parameters.
        """
        raise NotImplementedError('TBA')

    def get_cookie_params(self) -> dict[str, Any]:
        """
        Retrieve cookies.

        Retrieves cookies sent by the client to the server.

        The data MUST be compatible with the structure of the _COOKIE
        superglobal.

        Returns
        -------
        dict[str, Any]
            Dictionary of cookies. Cannot determine the correct type due JSON decoding.
        """
        raise NotImplementedError('TBA')

    def with_cookie_params(self, cookies: dict[str, Any]) -> 'ServerRequestInterface':
        """
        Return an instance with the specified cookies.

        The data IS NOT REQUIRED to come from the _COOKIE superglobal, but MUST
        be compatible with the structure of _COOKIE. Typically, this data will
        be injected at instantiation.

        This method MUST NOT update the related Cookie header of the request
        instance, nor related values in the server params.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        updated cookie values.

        Parameters
        ----------
        cookies: dict[str, Any]
            Dict of key/value pairs representing cookies.

        Returns
        -------
        ServerRequestInterface
        """
        raise NotImplementedError('TBA')

    def get_query_params(self) -> dict[str, Any]:
        """
        Retrieve query string arguments.

        Retrieves the deserialized query string arguments, if any.

        Note: the query params might not be in sync with the URI or server
        params. If you need to ensure you are only getting the original
        values, you may need to parse the query string from `get_uri().get_query()`
        or from the `QUERY_STRING` server param.

        Returns
        -------
        dict[str, Any]
        """
        raise NotImplementedError('TBA')

    def with_query_params(self, query: dict[str, Any]) -> 'ServerRequestInterface':
        """
        Return an instance with the specified query string arguments.

        These values SHOULD remain immutable over the course of the incoming
        request. They MAY be injected during instantiation, such as from PHP's
        _GET superglobal, or MAY be derived from some other value such as the
        URI. In cases where the arguments are parsed from the URI, the data
        MUST be compatible with what Python's `urllib` would return for
        purposes of how duplicate query parameters are handled, and how nested
        sets are handled.

        Setting query string arguments MUST NOT change the URI stored by the
        request, nor the values in the server params.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        updated query string arguments.

        Parameters
        ----------
        query: dict[str, Any]
            Dict of query string arguments, typically from _GET.

        Returns
        -------
        ServerRequestInterface
        """
        raise NotImplementedError('TBA')

    def get_uploaded_files(self) -> list[UploadedFileInterface]:
        """
        Retrieve normalized file upload data.

        This method returns upload metadata in a normalized tree, with each leaf
        an instance of pypsr.http.message.UploadedFileInterface.

        These values MAY be prepared from the message body during
        instantiation, or MAY be injected via with_uploaded_files().

        Returns
        -------
        list[UploadedFileInterface]
            A list of UploadedFileInterface instances; an empty list MUST
            be returned if no data is present.
        """
        raise NotImplementedError('TBA')

    def with_uploaded_files(self, uploaded_files: list[UploadedFileInterface]) -> 'ServerRequestInterface':
        """
        Create a new instance with the specified uploaded files.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        updated body parameters.

        Parameters
        ----------
        uploaded_files: list[UploadedFileInterface]
            A list of UploadedFileInterface instances.

        Returns
        -------
        ServerRequestInterface

        Raises
        ------
        AttributeError
            if an invalid structure is provided.
        """
        raise NotImplementedError('TBA')

    def get_parsed_body(self) -> list[object] | dict[str, str] | str | None:
        """
        Retrieve any parameters provided in the request body.

        If the request Content-Type is either application/x-www-form-urlencoded
        or multipart/form-data, and the request method is POST, this method MUST
        return the contents of _POST.

        Otherwise, this method may return any results of deserializing
        the request body content; as parsing returns structured content, the
        potential types MUST be list for multipart, dict for urlencoded or string
        for everything else (like JSON). A null value indicates the absence of
        body content.

        Returns
        -------
        list[object] | dict[str, str] | str | None
            The deserialized body parameters, if any. These will typically be an object.
        """
        raise NotImplementedError('TBA')

    def with_parsed_body(self, data: list[object] | dict[str, str] | str | None) -> 'ServerRequestInterface':
        """
        Return an instance with the specified body parameters.

        These MAY be injected during instantiation.

        If the request Content-Type is either application/x-www-form-urlencoded
        or multipart/form-data, and the request method is POST, use this method
        ONLY to inject the contents of _POST.

        The data IS NOT REQUIRED to come from _POST, but MUST be the results of
        deserializing the request body content. Deserialization/parsing returns
        structured data, and, as such, this method ONLY accepts lists of objects
        or dicts, or a None value if nothing was available to parse.

        As an example, if content negotiation determines that the request data
        is a JSON payload, this method could be used to create a request
        instance with the deserialized parameters.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        updated body parameters.

        Parameters
        ----------
        data: list[object] | dict[str, str] | str | None
            The deserialized body data. This will typically be in a list of objects
            (for multipart/form-data) or dict (for application/x-www-form-urlencoded)
            or string with own content type (like already encoded JSON).

        Returns
        -------
        ServerRequestInterface

        Raises
        ------
        AttributeError
            if an unsupported argument type is provided.
        """
        raise NotImplementedError('TBA')

    def get_attributes(self) -> dict[str, Any]:
        """
        Retrieve attributes derived from the request.

        The request "attributes" may be used to allow injection of any
        parameters derived from the request: e.g., the results of path
        match operations; the results of decrypting cookies; the results of
        deserializing non-form-encoded message bodies; etc. Attributes
        will be application and request specific, and CAN be mutable.

        Returns
        -------
        dict[str, Any]
            Attributes derived from the request.
        """
        raise NotImplementedError('TBA')

    def get_attribute(self, name: str, default: Any | None = None) -> Any:
        """
        Retrieve a single derived request attribute.

        Retrieves a single derived request attribute as described in
        get_attributes(). If the attribute has not been previously set, returns
        the default value as provided.

        This method obviates the need for a has_attribute() method, as it allows
        specifying a default value to return if the attribute is not found.

         * @see get_attributes()

        Parameters
        ----------
        name: str
            The attribute name.
        default: Any | None
            Default value to return if the attribute does not exist.

        Returns
        -------
        Any
        """
        raise NotImplementedError('TBA')

    def with_attribute(self, name: str, value: Any) -> 'ServerRequestInterface':
        """
        Return an instance with the specified derived request attribute.

        This method allows setting a single derived request attribute as
        described in getAttributes().

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        updated attribute.

         * @see getAttributes()

        Parameters
        ----------
        name: str
            The attribute name.
        value: Any
            The value of the attribute.

        Returns
        -------
        ServerRequestInterface
        """
        raise NotImplementedError('TBA')

    def without_attribute(self, name: str) -> 'ServerRequestInterface':
        """
        Return an instance that removes the specified derived request attribute.

        This method allows removing a single derived request attribute as
        described in getAttributes().

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that removes
        the attribute.

         * @see getAttributes()

        Parameters
        ----------
        name: str
            The attribute name.

        Returns
        -------
        ServerRequestInterface
        """
        raise NotImplementedError('TBA')


class ResponseInterface(MessageInterface):
    """
    Representation of an outgoing, server-side response.

    Per the HTTP specification, this interface includes properties for
    each of the following:

    - Protocol version
    - Status code and reason phrase
    - Headers
    - Message body

    Responses are considered immutable; all methods that might change state MUST
    be implemented such that they retain the internal state of the current
    message and return an instance that contains the changed state.
    """

    def get_status_code(self) -> int:
        """
        Gets the response status code.

        The status code is a 3-digit integer result code of the server's attempt
        to understand and satisfy the request.

        Returns
        -------
        int
            Status code.
        """
        raise NotImplementedError('TBA')

    def with_status(self, code: int, reason_phrase: str = '') -> 'ResponseInterface':
        """
        Return an instance with the specified status code and, optionally, reason phrase.

        If no reason phrase is specified, implementations MAY choose to default
        to the RFC 7231 or IANA recommended reason phrase for the response's
        status code.

        This method MUST be implemented in such a way as to retain the
        immutability of the message, and MUST return an instance that has the
        updated status and reason phrase.

         * @link https://tools.ietf.org/html/rfc7231#section-6
         * @link https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

        Parameters
        ----------
        code: int
            The 3-digit integer result code to set.
        reason_phrase: str
            The reason phrase to use with the provided status code; if none is provided,
            implementations MAY use the defaults as suggested in the HTTP specification.

        Returns
        -------
        ResponseInterface

        Raises
        ------
        AttributeError
            For invalid status code arguments.
        """
        raise NotImplementedError('TBA')

    def get_reason_phrase(self) -> str:
        """
        Gets the response reason phrase associated with the status code.

        Because a reason phrase is not a required element in a response
        status line, the reason phrase value MAY be null. Implementations MAY
        choose to return the default RFC 7231 recommended reason phrase (or those
        listed in the IANA HTTP Status Code Registry) for the response's
        status code.

         * @link https://tools.ietf.org/html/rfc7231#section-6
         * @link https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

        Returns
        -------
        string
            Reason phrase; must return an empty string if none present.
        """
        raise NotImplementedError('TBA')


class RequestFactoryInterface:

    def create_request(self, method: str, uri: str | UriInterface) -> RequestInterface:
        """
        Create a new request.

        Parameters
        ----------
        method: str
            The HTTP method associated with the request.
        uri: str | UriInterface
            The URI associated with the request.

        Returns
        -------
        RequestInterface
        """
        raise NotImplementedError('TBA')


class ResponseFactoryInterface:

    def create_response(self, code: int = 200, reason_phrase: str = '') -> ResponseInterface:
        """
        Create a new response.


        Parameters
        ----------
        code: int
            The HTTP status code. Defaults to 200.
        reason_phrase: string
            The reason phrase to associate with the status code
            in the generated response. If none is provided, implementations MAY use
            the defaults as suggested in the HTTP specification.

        Returns
        -------
        ResponseInterface
        """
        raise NotImplementedError('TBA')


class ServerRequestFactoryInterface:

    def create_server_request(
            self,
            method: str, uri: str | UriInterface,
            server_params: dict[str, str | int | bool] | None = None,
    ) -> ServerRequestInterface:
        """
        Create a new server request.

        Note that server parameters are taken precisely as given - no parsing/processing
        of the given values is performed. In particular, no attempt is made to
        determine the HTTP method or URI, which must be provided explicitly.

        Parameters
        ----------
        method: str
            The HTTP method associated with the request.
        uri: str | UriInterface
            The URI associated with the request.
        server_params: dict[str, str | int | bool] | None
            A dictionary of Server API (SAPI) parameters with which to seed the generated request instance.

        Returns
        -------
        ServerRequestInterface
        """
        raise NotImplementedError('TBA')


class StreamFactoryInterface:

    def create_stream(self, content: str = '') -> BytesIO:
        """
        Create a new stream from a string.

        The stream SHOULD be created with a temporary resource.

        Parameters
        ----------
        content: str
            String content with which to populate the stream.

        Returns
        -------
        BytesIO
        """
        raise NotImplementedError('TBA')

    def create_stream_from_file(self, filename: str, mode: str = 'r') -> BytesIO:
        """
        Create a stream from an existing file.

        The file MUST be opened using the given mode, which may be any mode
        supported by the `open` function.

        The `filename` MAY be any string supported by `open()`.

        Parameters
        ----------
        filename: str
            The filename or stream URI to use as basis of stream.
        mode: str
            The mode with which to open the underlying filename/stream.

        Returns
        -------
        BytesIO

        Raises
        ------
        RuntimeError
            If the file cannot be opened.
        AttributeError
            If the mode is invalid.
        """
        raise NotImplementedError('TBA')

    def create_stream_from_resource(self, resource) -> BytesIO:
        """
        Create a new stream from an existing resource.

        The stream MUST be readable and may be writable.

        Parameters
        ----------
        resource
            The Pythonic resource to use as the basis for the stream.

        Returns
        -------
        BytesIO
        """
        raise NotImplementedError('TBA')


class UploadedFileFactoryInterface:

    def create_uploaded_file(
            self,
            stream: BytesIO,
            size: int | None = None,
            error: int = 0,
            client_filename: str | None = None,
            client_media_type: str | None = None,
    ) -> UploadedFileInterface:
        """
        Create a new uploaded file.

        If a size is not provided it will be determined by checking the size of
        the stream.

        * @link https://php.net/manual/features.file-upload.post-method.php
        * @link https://php.net/manual/features.file-upload.errors.php

        Parameters
        ----------
        stream: BytesIO
            The underlying stream representing the uploaded file content.
        size: int
            The size of the file in bytes.
        error: int
            The PHP file upload error.
        client_filename: str | None
            The filename as provided by the client, if any.
        client_media_type: str | None
            The media type as provided by the client, if any.

        Returns
        -------
        UploadedFileInterface

        Raises
        ------
        AttributeError
            If the file resource is not readable
        """
        raise NotImplementedError('TBA')


class UriFactoryInterface:

    def create_uri(self, uri: str = '') -> UriInterface:
        """
        Create a new URI.

        Parameters
        ----------
        uri: str
            The URI to parse.

        Returns
        -------
        UriInterface

        Raises
        ------
        AttributeError
            If the given URI cannot be parsed.
        """
        raise NotImplementedError('TBA')
