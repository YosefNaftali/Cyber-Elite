from CpeTransformer import CpeTransformer
from InstalledPkgMiner import InstalledPkgMiner
from NvdClient import NvdClient

miner = InstalledPkgMiner()
transformer = CpeTransformer()
nvd_client = NvdClient()


class Search:
    def __init__(self):
        pass

    def search_machine(self):
        result = []
        installed_packages = miner.get_installed_packages_details()
        installed_packages = [('7-zip', '3.13'), ('7-zip', '4.20'), ('excel', '*')]
        packages_cpe_schema = transformer.get_cpe_schema_for_packages(installed_packages)
        for cpe_schema in packages_cpe_schema:
            try:
                cpes = nvd_client.get_cpes_from_nvd(cpe_schema[1])
                cves = nvd_client.get_matches_cve_to_cpe_list(cpes)
                result.append((cpe_schema[0], cves))
            except Exception as e:
                e.args += 'Search ' + 'search_machine'
                raise
        return result
