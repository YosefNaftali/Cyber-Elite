from tabulate import tabulate

class Printer:
    def __init__(self):
        pass

    def _dic_to_list_converter(self, data_dict):
        result = []
        for key, value in data_dict.items():
            try:
                temp = ['  '.join(key), '\n'.join(value)]
                result.append(temp)
            except Exception as e:
                pass
        return result

    def print(self, data, headers):
        data_list = self._dic_to_list_converter(data)
        table = tabulate(data_list, headers=headers, tablefmt='grid')
        print(table)