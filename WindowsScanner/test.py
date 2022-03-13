# Script to get all installed packages
import winreg

PATH_TO_INSTALLED_PACKAGES = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'


def get_installed_packages_details():
    result = []
    try:
        # Get handle to all installed packages
        packages_handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PATH_TO_INSTALLED_PACKAGES, reserved=0,
                                         access=winreg.KEY_READ)

        index = 0
        try:
            while True:
                # Generates the full path in Registry of each installed pkg
                installed_pkg_path = PATH_TO_INSTALLED_PACKAGES + '\\' + winreg.EnumKey(packages_handle, index)

                # Retrieves the values of each installed pkg
                pkg_details = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, installed_pkg_path, reserved=0,
                                             access=winreg.KEY_READ)
                try:
                    print(installed_pkg_path)
                    print(winreg.QueryValueEx(pkg_details, "DisplayName")[0])


                except OSError as e:
                    pass

                index += 1
        except OSError as e:
            winreg.CloseKey(packages_handle)
            return result
    except Exception as e:
        raise e





get_installed_packages_details()
