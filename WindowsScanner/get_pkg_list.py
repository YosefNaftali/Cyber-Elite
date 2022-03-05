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
                        pkg_name = winreg.QueryValueEx(pkg_details, "DisplayName")[0]
                        pkg_version = winreg.QueryValueEx(pkg_details, "DisplayVersion")[0]
                        result.append((pkg_name, pkg_version))
                    except OSError as e:
                        pass

                    index += 1
            except OSError as e:
                return result
    except Exception as e:
        raise e


def print_pkg_details():
    try:
        for pkg in get_installed_packages_details():
            print('Name:', pkg[0], 'Version:', pkg[1])
    except Exception as e:
        print(e)


print_pkg_details()
