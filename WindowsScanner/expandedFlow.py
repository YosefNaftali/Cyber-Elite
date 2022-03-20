from InstalledPkgMiner import *
from CpeTransformer import *
from NvdClient import *
from Printer import *


def expandedFlow():
    try:
        miner = InstalledPkgMiner()
        transformer = CpeTransformer()
        nvd_client = NvdClient()
        printer = Printer()

        installed_packages = miner.get_installed_packages_details()
        # installed_packages = [('7-zip', '3.13'), ('7-zip', '4.20'), ('excel', '*')]
        expanded_iterations = get_maximum_len_of_product_key(installed_packages)
        packages_cpe_schema = transformer.get_cpe_schema_for_packages(installed_packages)
        installed_packages_cve = nvd_client.get_packages_cve(packages_cpe_schema)
        printer.print(installed_packages_cve, ['Package Name', 'CVE ID'])
        while expanded_iterations > 0:
            installed_packages = cut_all_long_names(installed_packages)
            packages_cpe_schema = transformer.get_cpe_schema_for_packages(installed_packages)
            installed_packages_cve = nvd_client.get_packages_cve(packages_cpe_schema)
            printer.print(installed_packages_cve, ['Package Name', 'CVE ID'])
            expanded_iterations -= 1

    except Exception as e:
        print(e)


def cut_long_name(name):
    short_name = name.split(" ")[:-1:1]
    if len(short_name) > 0:
        return " ".join(short_name)
    return name


def get_maximum_len_of_product_key(installed_packages):
    maximum = 0
    for pkg in installed_packages:
        temp_max = pkg[0].split(" ")[:-1:1]
        len_temp_max = len(temp_max)
        maximum = len_temp_max if maximum < len_temp_max else maximum
    return maximum


def cut_all_long_names(installed_packages):
    result = []
    for pkg in installed_packages:
        result.append((cut_long_name(pkg[0]), pkg[1]))
    return result


expandedFlow()
