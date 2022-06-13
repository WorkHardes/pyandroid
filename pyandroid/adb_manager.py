import usb

import i_adb_manager


ADB_CLASS = 0xFF
ADB_SUBCLASS = 0x42
ADB_PROTOCOL = 0x01


class AdbManager(i_adb_manager.IAdbManager):
    def __init__(self) -> None:
        pass

    @staticmethod
    def devices() -> list[str]:
        fastboot_devices: list[str] = []
        for device in usb.core.find(find_all=True):
            for cfg in device:
                dev = usb.util.find_descriptor(
                    cfg,
                    bInterfaceClass=ADB_CLASS,
                    bInterfaceSubClass=ADB_SUBCLASS,
                    bInterfaceProtocol=ADB_PROTOCOL,
                )
                if dev is None:
                    continue
                else:
                    try:
                        fastboot_devices.append(device.serial_number)
                    except (usb.core.USBError, ValueError):
                        # Start server from sudo for full usb access
                        pass
        return fastboot_devices
