from pyandroid import adb_manager


ADB_DEVICES = [""]


def main() -> None:
    adb_devices = adb_manager.AdbManager.devices()
    print("devices:", adb_devices)
    if adb_devices == ADB_DEVICES:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
