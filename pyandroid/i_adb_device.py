import abc


class IAdbDevice(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def shell(self, cmd: str) -> bytes:
        raise NotImplementedError
