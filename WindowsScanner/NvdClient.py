import requests

CPE_REST_API = 'https://services.nvd.nist.gov/rest/json/cpes/1.0/'
CVE_REST_API = 'https://services.nvd.nist.gov/rest/json/cves/1.0/'
CPE_RESULT_AMOUNT = '1'
CVE_RESULT_AMOUNT_PER_CPE = '40'


class NvdClient:
    def __init__(self):
        self.severities = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']

    def _get_product_cpe_list(self, product_cpe_schema):
        result = []
        try:
            url = CPE_REST_API + "?resultsPerPage=" + CPE_RESULT_AMOUNT + "&" + "cpeMatchString=" + product_cpe_schema
            res = requests.get(url=url)
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
                res = requests.get(url=url)
                result += (self._response_pharser(res, 'cve'))
                return result
        except Exception as e:
            e.args += 'NvdClient' + '_get_product_cve_list'
            raise
        finally:
            return result

    def _get_product_cve_list_for_cpe(self, cpe, severity):
        result = []
        url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString="
        try:
            url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString=" + cpe
            if severity == 'Default':
                for sev in self.severities:
                    url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString=" + cpe +\
                          "&cvssV3Severity=" + sev
                    res = requests.get(url=url)
                    result.append((sev, self._response_pharser(res, 'cve')))
            else:
                url = CVE_REST_API + "?resultsPerPage=" + CVE_RESULT_AMOUNT_PER_CPE + "&" + "cpeMatchString=" + cpe +\
                      "&cvssV3Severity=" + severity

                res = requests.get(url=url)
                result.append((severity, self._response_pharser(res, 'cve')))
            return result
        except Exception as e:
            e.args += 'NvdClient' + '_get_product_cve_list'
            raise
        finally:
            return result

    def _response_pharser(self, res, req_type):
        result = []
        try:
            res = res.json()
            if req_type == 'cpe':
                cpe_data = res['result']['cpes']
                for cpe in cpe_data:
                    result.append(cpe['cpe23Uri'])
            elif req_type == 'cve':
                cve_data = res['result']['CVE_Items']
                for cve in cve_data:
                    result.append(cve['cve']['CVE_data_meta']['ID'])
        except TypeError as e:
            raise
        except Exception as e:
            raise
        finally:
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

    def get_matches_cve_to_cpe_list(self, cpe_list, severity):
        result = []
        if cpe_list is None:
            return result
        for cpe in cpe_list:
            try:
                cve_list = self._get_product_cve_list_for_cpe(cpe, severity)
                #result.append(cve_list)
                result += cve_list
            except Exception as e:
                raise
        return result


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
            res = requests.get(url=url)
            if res.status_code != 200:
                if self.len_of_product_from_cpe(product_cpe_schema) > 1:
                    return self.expended_get_product_cpe_list(self.create_new_short_cpe(product_cpe_schema))
                else:
                    return result
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

