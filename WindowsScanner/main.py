
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from CPEtransformer import *
from NvdClient import *


def main():
    try:
        transformer = CpeTransformer()
        nvd_client = NvdClient()
        cpe_schema = transformer.get_cpe_schema_from_package('7-zip')
        print(cpe_schema)
        list_cpe = nvd_client.get_list_of_cpe(cpe_schema)
        print(len(list_cpe))
    except Exception as e:
        print(e)





if __name__ == '__main__':
    main()

