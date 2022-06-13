import i_adb_device


class AdbDevice(i_adb_device.IAdbDevice):
    def __init__(self) -> None:
        pass

    def shell(self, cmd: str) -> bytes:
        raise NotImplementedError
