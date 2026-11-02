
class ContainerExceptionInterface(Exception):
    """
    Base interface representing a generic exception in a container.
    """
    pass


class NotFoundExceptionInterface(ContainerExceptionInterface):
    """
    No entry was found in the container.
    """
    pass
