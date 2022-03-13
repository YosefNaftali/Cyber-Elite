CPE_VERSION = 'cpe:2.3'


class CpeTransformer:
    def __init__(self):
        pass

    def _create_cpe_from_data(self, part='a', vendor='*', product='*', version='*', update='*', edition='*',
                             language='*'):
        # cpe:2.3:o:microsoft:windows_10:1511
        return CPE_VERSION + ":" + part + ":" + vendor + ":" + product + ":" + version + ":" + update + \
               ":" + edition + ":" + language

    def get_cpe_schema_for_packages(self, installed_packages_list):
        result = []
        for pkg in installed_packages_list:
            pkg_cpe = self._create_cpe_from_data(product=pkg[0], version=pkg[1])
            result.append((pkg, pkg_cpe))
        return result
