# Script to get all installed packages
import winreg

PATH_TO_INSTALLED_PACKAGES = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'


class InstalledPkgMiner:
    def __init__(self):
        pass

    # Returns handle to all installed packages in Registry
    def _get_handle_to_installed_packages(self):
        try:
            installed_packages_handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PATH_TO_INSTALLED_PACKAGES,
                                                       reserved=0, access=winreg.KEY_READ)
            return installed_packages_handle
        except Exception as e:
            raise e

    def _get_pkg_name_and_version(self, installed_pkg_path):
        try:
            # Retrieves the values of each installed pkg
            pkg_details = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, installed_pkg_path, reserved=0,
                                         access=winreg.KEY_READ)
            try:
                pkg_name = winreg.QueryValueEx(pkg_details, "DisplayName")[0]
                pkg_version = winreg.QueryValueEx(pkg_details, "DisplayVersion")[0]
                winreg.CloseKey(pkg_details)
                return pkg_name, pkg_version
            except OSError as e:
                pass
        except Exception as e:
            raise e

    # Returns name and version of installed packages
    def _get_installed_packages_details(self, installed_packages_handle):
        try:
            result = []
            index = 0
            try:
                # Iterate on all installed packages in Registry
                while True:
                    # Generates the full path in Registry of each installed pkg
                    installed_pkg_path = PATH_TO_INSTALLED_PACKAGES + '\\' + winreg.EnumKey(installed_packages_handle, index)
                    try:
                        pkg_name, pkg_version = self._get_pkg_name_and_version(installed_pkg_path)
                        result.append((pkg_name, pkg_version))
                    except TypeError as e:
                        # When we try to get name and version of non exist pkg
                        pass
                    index += 1
            except OSError as e:
                # When we try to get key after the last one in the Registry
                return result
        except Exception as e:
            raise e

    def get_installed_packages_details(self):
        try:
            # Get handle to all installed packages
            packages_handle = self._get_handle_to_installed_packages()
            # Get list of name and version of installed packages
            installed_packages_details = self._get_installed_packages_details(packages_handle)
            # Close the handle
            winreg.CloseKey(packages_handle)
            return installed_packages_details
        except Exception as e:
            raise e

