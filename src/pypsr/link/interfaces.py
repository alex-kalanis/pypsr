from typing import Iterable


class LinkInterface:
    """
    A readable link object.
    """

    def get_href(self) -> str:
        """
        Returns the target of the link.

        The target link must be one of:

        - An absolute URI, as defined by RFC 5988.
        - A relative URI, as defined by RFC 5988. The base of the relative link
          is assumed to be known based on context by the client.
        - A URI template as defined by RFC 6570.

        If a URI template is returned, is_templated() MUST return True.

        Returns
        -------
        string
        """
        raise NotImplementedError('TBA')

    def is_templated(self) -> bool:
        """
        Returns whether or not this is a templated link.

        Returns
        -------
        bool
            True if this link object is templated, False otherwise.
        """
        raise NotImplementedError('TBA')

    def get_rels(self) -> list[str]:
        """
        Returns the relationship type(s) of the link.

        This method returns 0 or more relationship types for a link, expressed
        as a list of strings.

        Returns
        -------
        list[str]
        """
        raise NotImplementedError('TBA')

    def get_attributes(self) -> dict[str, str | list[str]]:
        """
        Returns a list of attributes that describe the target URI.

        Returns
        -------
        dict[str, str | list[str]]
            A key-value list of attributes, where the key is a string and the value
            is either a Python primitive or a list of Python strings. If no values are
            found an empty array MUST be returned.
        """
        raise NotImplementedError('TBA')


class EvolvableLinkInterface(LinkInterface):
    """
    An evolvable link value object.
    """

    def with_href(self, href: str) -> 'EvolvableLinkInterface':
        """
        Returns an instance with the specified href.

        An implementing library SHOULD evaluate a passed object to a string
        immediately rather than waiting for it to be returned later.

        Parameters
        ----------
        href: str
            The href value to include. It must be one of:

            - An absolute URI, as defined by RFC 5988.
            - A relative URI, as defined by RFC 5988. The base of the relative link
              is assumed to be known based on context by the client.
            - A URI template as defined by RFC 6570.
            - An object implementing __str__() that produces one of the above
              values.

        Returns
        -------
        EvolvableLinkInterface
        """
        raise NotImplementedError('TBA')

    def with_rel(self, rel: str) -> 'EvolvableLinkInterface':
        """
        Returns an instance with the specified relationship included.

        If the specified rel is already present, this method MUST return
        normally without errors, but without adding the rel a second time.

        Parameters
        ----------
        rel: str
            The relationship value to add.

        Returns
        -------
        EvolvableLinkInterface
        """
        raise NotImplementedError('TBA')

    def without_rel(self, rel: str) -> 'EvolvableLinkInterface':
        """
        Returns an instance with the specified relationship excluded.

        If the specified rel is already not present, this method MUST return
        normally without errors.

        Parameters
        ----------
        rel: str
            The relationship value to exclude.

        Returns
        -------
        EvolvableLinkInterface
        """
        raise NotImplementedError('TBA')

    def with_attribute(self, attribute: str, value: str) -> 'EvolvableLinkInterface':
        """
        Returns an instance with the specified attribute added.

        If the specified attribute is already present, it will be overwritten
        with the new value.

        Parameters
        ----------
        attribute: str
            The attribute to include.
        value: str
            The value of the attribute to set.

        Returns
        -------
        EvolvableLinkInterface
        """
        raise NotImplementedError('TBA')

    def without_attribute(self, attribute: str) -> 'EvolvableLinkInterface':
        """
        Returns an instance with the specified attribute excluded.

        If the specified attribute is not present, this method MUST return
        normally without errors.

        Parameters
        ----------
        attribute: str
            The attribute to remove.

        Returns
        -------
        EvolvableLinkInterface
        """
        raise NotImplementedError('TBA')


class LinkProviderInterface:
    """
    A link provider object.
    """

    def get_links(self) -> Iterable[LinkInterface] | list[LinkInterface]:
        """
        Returns an iterable of LinkInterface objects.

        The iterable may be a list or any Python Iterable object. If no links
        are available, an empty list or Iterable MUST be returned.

        Returns
        -------
        Iterable[LinkInterface] | list[LinkInterface]
        """
        raise NotImplementedError('TBA')

    def get_links_by_rel(self, rel: str) -> Iterable[LinkInterface] | list[LinkInterface]:
        """
        Returns an iterable of LinkInterface objects that have a specific relationship.

        The iterable may be a list or any Python Iterable object. If no links
        with that relationship are available, an empty list or Iterable MUST be returned.

        Returns
        -------
        Iterable[LinkInterface] | list[LinkInterface]
        """
        raise NotImplementedError('TBA')


class EvolvableLinkProviderInterface(LinkProviderInterface):
    """
    An evolvable link provider value object.
    """

    def with_link(self, link: LinkInterface) -> 'EvolvableLinkProviderInterface':
        """
        Returns an instance with the specified link included.

        If the specified link is already present, this method MUST return normally
        without errors. The link is present if `link` is == identical to a link
        object already in the collection.

        Parameters
        ----------
        link: LinkInterface
            A link object that should be included in this collection.

        Returns
        -------
        EvolvableLinkProviderInterface
        """
        raise NotImplementedError('TBA')

    def without_link(self, link: LinkInterface) -> 'EvolvableLinkProviderInterface':
        """
        Returns an instance with the specified link removed.

        If the specified link is not present, this method MUST return normally
        without errors. The link is present if $link is === identical to a link
        object already in the collection.

        Parameters
        ----------
        link: LinkInterface
            The link to remove.

        Returns
        -------
        EvolvableLinkProviderInterface
        """
        raise NotImplementedError('TBA')
