import abc


class IAdbManager(abc.ABC):
    def __init__(self) -> None:
        pass

    @staticmethod
    @abc.abstractmethod
    def devices() -> list[str]:
        raise NotImplementedError
