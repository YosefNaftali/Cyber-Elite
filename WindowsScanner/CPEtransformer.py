
class CpeTransformer:

    def __init__(self):
        self.cpe2dot3 = "cpe:2.3"


    def create_cpe_from_data(self, part='a', vendor='*', product='*', version='*', update='*', edition='*',
                             language='*'):
        # cpe:2.3:o:microsoft:windows_10:1511
        return self.cpe2dot3 + ":" + part + ":" + vendor + ":" + product + ":" + version + ":" + update + ":" + edition + ":" + language

    def get_cpe_schema_from_package(self, name, version='*'):
        return self.create_cpe_from_data(product=name, version=version)
