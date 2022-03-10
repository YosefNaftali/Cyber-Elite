import requests

resultsPerPage = '2000'


# api-endpoint
REST_API_URL = "https://services.nvd.nist.gov/rest/json/cpes/1.0/"

# test_url = "https://services.nvd.nist.gov/rest/json/cpes/1.0/?cpeMatchString=cpe:2.3:a:microsoft:sql_server:2014:sp2"



class NvdClient:
    def __init__(self):
        return

    def get_list_of_cpe(self, query_parametr):
        result = []
        try:
            url = REST_API_URL + "?resultsPerPage="+ resultsPerPage+ "&" + "cpeMatchString=" + query_parametr
            res = requests.get(url=url).json()
            cpes_data = res['result']['cpes']
            for cpe in cpes_data:
                result.append(cpe['cpe23Uri'])
            return result
        except Exception as e:
            print(e)
            return result

    def get_list_of_cve(self):
        return "TODO"


