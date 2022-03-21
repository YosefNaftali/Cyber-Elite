from unittest import TestCase

from expandedFlow import cut_long_name


class Test(TestCase):
    def test_cut_long_name(self):
        result_1 = cut_long_name("7-Zip 19.00 (x64)")
        expected_1 = "7-Zip 19.00"
        result_2 = cut_long_name("7-Zip")
        expected_2 = "7-Zip"
        self.assertTrue(expected_1 == result_1 and expected_2 == result_2)
