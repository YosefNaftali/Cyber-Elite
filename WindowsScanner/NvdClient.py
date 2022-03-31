import requests

CPE_REST_API = 'https://services.nvd.nist.gov/rest/json/cpes/1.0/'
CVE_REST_API = 'https://services.nvd.nist.gov/rest/json/cves/1.0/'
CPE_RESULT_AMOUNT = '1'
CVE_RESULT_AMOUNT_PER_CPE = '3'

class NvdClient:
    def __init__(self):
        pass

    def _get_product_cpe_list(self, product_cpe_schema):
        result = None
        try:
            url = CPE_REST_API + "?resultsPerPage=" + CPE_RESULT_AMOUNT + "&" + "cpeMatchString=" + product_cpe_schema
            res = requests.get(url=url).json()
            result = self._response_pharser(res, 'cpe')
            return result
        except Exception as e:
            e += 'NvdClient' + '_get_product_cpe_list'
            raise
        finally:
            return result

    def _get_product_cve_list(self, product_cpe_list):
        result = []
        url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString="
        try:
            for cpe in product_cpe_list:
                url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString="
                url += cpe
                res = requests.get(url=url).json()
                result += (self._response_pharser(res, 'cve'))
                return result
        except Exception as e:
            e.args += 'NvdClient' + '_get_product_cve_list'
            raise
        finally:
            return result

    def _get_product_cve_list_for_cpe(self, cpe):
        result = []
        url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString="
        try:
            url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString="
            url += cpe
            res = requests.get(url=url).json()
            result += (self._response_pharser(res, 'cve'))
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

    def get_cpes_from_nvd(self, installed_cpe_schema):
        result = []
        try:
            cpe_list = self._get_product_cpe_list(installed_cpe_schema)
            result = cpe_list
        except Exception as e:
            raise
        return result

    def get_matches_cve_to_cpe(self, cpe):
        result = []
        try:
            cve_list = self._get_product_cve_list(cpe)
            result = cve_list
        except Exception as e:
            raise
        return result

    def get_matches_cve_to_cpe_list(self, cpe_list):
        result = []
        if cpe_list is None:
            return result
        try:
            for cpe in cpe_list:
                cve_list = self._get_product_cve_list_for_cpe(cpe)
                # result.append(cve_list)
                result += cve_list
        except Exception as e:
            raise
        return result

   #def get_packages_cve(self, installed_packages_cpe_schema):
   #    result = {}
   #    for cpe_schema in installed_packages_cpe_schema:
   #        try:
   #            cpe_list = self._get_product_cpe_list(cpe_schema[1])
   #            cve_list = self._get_product_cve_list(cpe_list)
   #            result[cpe_schema[0]] = cve_list
   #        except Exception as e:
   #            e.args += 'NvdClient' + 'get_packages_cve'
   #            raise
   #    return result
    def get_expended_cpes_from_nvd(self, installed_cpe_schema):
        result = []
        try:
            cpe_list = self.expended_get_product_cpe_list(installed_cpe_schema)
            result = cpe_list
        except Exception as e:
            raise
        return result

    def expended_get_product_cpe_list(self, product_cpe_schema):
        result = None
        try:
            url = CPE_REST_API + "?resultsPerPage=" + CPE_RESULT_AMOUNT + "&" + "cpeMatchString=" + product_cpe_schema
            res = requests.get(url=url).json()
            if res == {'message': 'Invalid CPE string provided'} and self.len_of_product_from_cpe(product_cpe_schema) > 1:
                return self.expended_get_product_cpe_list(self.create_new_short_cpe(product_cpe_schema))
            result = self._response_pharser(res, 'cpe')
            return result
        except Exception as e:
            e += 'NvdClient' + '_get_product_cpe_list'
            raise


    def len_of_product_from_cpe(self, cpe):
        product = self.extract_product_fild_from_cpe(cpe)
        return len(product.split(' '))

    def extract_product_fild_from_cpe(self, cpe):
        return cpe.split(':')[4]

    def create_new_short_cpe(self, cpe):
        result = cpe.split(':')
        result[4] = ' '.join(self.extract_product_fild_from_cpe(cpe).split(" ")[:-1:1])
        return ':'.join(result)

