from typing import TypeVar

TC = TypeVar('TC')  # Type of Class


class ContainerInterface:
    """
    Describes the interface of a container that exposes methods to read its entries.
    """

    def get(self, cls: str | type[TC]) -> TC:
        """
        Finds an entry of the container by its identifier and returns it.

        Parameters
        ----------
        cls: string | type[TC]
            Identifier of the entry to look for.

        Returns
        -------
        TC
            Entry

        Raises
        ------
        pypsr.container.exceptions.NotFoundExceptionInterface
            No entry was found for **this** identifier.
        pypsr.container.exceptions.ContainerExceptionInterface
            Error while retrieving the entry.
        """
        raise NotImplementedError('TBA')

    def has(self, cls: str | type[TC]) -> bool:
        """
        Returns true if the container can return an entry for the given identifier immediately. Returns false otherwise.

        `has(cls)` returning true does not mean that `get(cls)` will not throw an exception.
        It does however mean that `get(cls)` will not throw a `NotFoundExceptionInterface`.

        Parameters
        ----------
        cls: string | type[TC]
            Identifier of the entry to look for.

        Returns
        -------
        bool
        """
        raise NotImplementedError('TBA')
