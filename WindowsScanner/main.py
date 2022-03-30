from InstalledPkgMiner import *
from CpeTransformer import *
from NvdClient import *
from Printer import *
from Search import Search


def main():

    try:
        printer = Printer()
        searcher = Search()
        search_data = searcher.search_machine()
        printer.print_tuple_to_chart(search_data, ['Package Name', 'CVE ID'])

        #miner = InstalledPkgMiner()
        #transformer = CpeTransformer()
        #nvd_client = NvdClient()
        #printer = Printer()
#
        #installed_packages = miner.get_installed_packages_details()
        #installed_packages = [('7-zip', '3.13'), ('7-zip', '4.20'), ('excel', '*')]
        #packages_cpe_schema = transformer.get_cpe_schema_for_packages(installed_packages)
        #installed_packages_cve = nvd_client.get_packages_cve(packages_cpe_schema)
        #printer.print(installed_packages_cve, ['Package Name', 'CVE ID'])

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
