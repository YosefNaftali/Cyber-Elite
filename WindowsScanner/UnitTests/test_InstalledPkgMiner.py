from unittest import TestCase

from InstalledPkgMiner import InstalledPkgMiner

installedPkgMiner = InstalledPkgMiner()


class TestInstalledPkgMiner(TestCase):
    def test_get_installed_packages_details(self):
        installed_packages_details = installedPkgMiner.get_installed_packages_details()
        self.assertTrue(len(installed_packages_details) > 1)

    def test_prnit_get_installed_packages_details(self):
        installed_packages_details = installedPkgMiner.get_installed_packages_details()
        print(installed_packages_details)
        self.assertTrue(len(installed_packages_details) > 1)
