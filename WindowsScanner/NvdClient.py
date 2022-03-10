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
            url = self.create_url_to_nvd_api(query_parametr)
            res = requests.get(url=url).json()
            result = self.get_list_cpe_from_nvd_respone(res)
            return result
        except Exception as e:
            print(e)
            return result

    def get_list_of_cve(self, cpe_list):
        return "TODO"

    def get_list_cpe_from_nvd_respone(self, res):
        result = []
        cpe_data = res['result']['cpes']
        for cpe in cpe_data:
            result.append(cpe['cpe23Uri'])
        return result

    def create_url_to_nvd_api(self, query_parametr):
        return REST_API_URL + "?resultsPerPage=" + resultsPerPage + "&" + "cpeMatchString=" + query_parametr


