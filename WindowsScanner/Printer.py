from tabulate import tabulate


class Printer:
    def __init__(self):
        pass

    def _tuple_to_list_converter(self, data_dict):
        result = []
        for item in data_dict:
            try:
                cves = []
                severity_list = []
                for sev in item[1]:
                    if len(sev[1]) > 0:
                        cves += sev[1]
                        severity_string = [sev[0]] * len(sev[1])
                        severity_list += severity_string
                temp = [' '.join(item[0]), '\n'.join(cves), '\n'.join(severity_list)]
                result.append(temp)
            except Exception as e:
                print(e)
        return result

    def print_tuple_to_chart(self, data, headers):
        data_list = self._tuple_to_list_converter(data)
        table = tabulate(data_list, headers=headers, tablefmt='grid')
        print(table)
