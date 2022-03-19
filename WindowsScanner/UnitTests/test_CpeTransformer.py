from unittest import TestCase
from CpeTransformer import CpeTransformer

LIST_OF_PKG = "[{['7-zip'], ['19']}, {['windows_10'], ['1511']}]"
transfer = CpeTransformer()


class TestCpeTransformer(TestCase):
    def test_get_cpe_schema_for_packages(self):
        list_of_pkg = [('7-zip', '19'), ('xampp', '1.5.2')]
        expected = [(('7-zip', '19'), 'cpe:2.3:a:*:7-zip:19:*:*:*'),
                    (('xampp', '1.5.2'), 'cpe:2.3:a:*:xampp:1.5.2:*:*:*')]
        self.assertTrue(transfer.get_cpe_schema_for_packages(list_of_pkg) == expected)
