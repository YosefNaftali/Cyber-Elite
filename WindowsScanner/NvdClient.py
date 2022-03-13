import requests

CPE_REST_API = 'https://services.nvd.nist.gov/rest/json/cpes/1.0/'
CVE_REST_API = 'https://services.nvd.nist.gov/rest/json/cves/1.0/'
RESULT_AMOUNT = '2000'


class NvdClient:
    def __init__(self):
        pass

    def _get_product_cpe_list(self, product_cpe_schema):
        result = None
        try:
            url = CPE_REST_API + "?resultsPerPage=" + RESULT_AMOUNT + "&" + "cpeMatchString=" + product_cpe_schema
            res = requests.get(url=url).json()
            result = self._response_pharser(res, 'cpe')
            return result
        except Exception as e:
            e += 'NvdClient' + '_get_product_cpe_list'
            raise
        finally:
            return result

    def _get_product_cve_list(self, product_cpe_list):
        result = None
        url = CVE_REST_API + "?resultsPerPage=" + RESULT_AMOUNT + "&" + "cpeMatchString="
        try:
            for cpe in product_cpe_list:
                url += cpe
                res = requests.get(url=url).json()
                result = self._response_pharser(res, 'cve')
                return result
        except Exception as e:
            e.args += 'NvdClient' + '_get_product_cve_list'
            raise
        finally:
            return result


    def _response_pharser(self, res, req_type):
        result = []
        if req_type == 'cpe':
            cpe_data = res['result']['cpes']
            for cpe in cpe_data:
                result.append(cpe['cpe23Uri'])
        elif req_type == 'cve':
            cve_data = res['result']['CVE_Items']
            for cve in cve_data:
                result.append(cve['cve']['CVE_data_meta']['ID'])
        return result


    def get_packages_cve(self, installed_packages_cpe_schema):
        result = {}
        for cpe_schema in installed_packages_cpe_schema:
            try:
                cpe_list = self._get_product_cpe_list(cpe_schema[1])
                cve_list = self._get_product_cve_list(cpe_list)
                result[cpe_schema[0]] = cve_list
            except Exception as e:
                e.args += 'NvdClient' + 'get_packages_cve'
                raise
        return result


