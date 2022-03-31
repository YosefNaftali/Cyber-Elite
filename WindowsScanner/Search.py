from CpeTransformer import CpeTransformer
from InstalledPkgMiner import InstalledPkgMiner
from NvdClient import NvdClient
RUN_EXPANDED_SCAN = 'True'
miner = InstalledPkgMiner()
transformer = CpeTransformer()
nvd_client = NvdClient()


class Search:
    def __init__(self):
        pass

    def search_machine(self):
        result = []
        installed_packages = miner.get_installed_packages_details()
        installed_packages = [('7-zip', '4.20'), ('7-zip (x64)', '3.13'), ('vpnremote', '4.2.32'),  ('outlook', '2016')]
        packages_cpe_schema = transformer.get_cpe_schema_for_packages(installed_packages)
        for cpe_schema in packages_cpe_schema:
            print(cpe_schema)
            try:
                if RUN_EXPANDED_SCAN == 'True':
                    cpes = nvd_client.get_expended_cpes_from_nvd(cpe_schema[1])
                else:
                    cpes = nvd_client.get_cpes_from_nvd(cpe_schema[1])
                cves = nvd_client.get_matches_cve_to_cpe_list(cpes)
                result.append((cpe_schema[0], cves))
            except Exception as e:
                e.args += 'Search ' + 'search_machine'
                raise
        return result
