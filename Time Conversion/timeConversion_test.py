import unittest
import sys
from io import StringIO

import timeConversion

class TimeConversionTestCase(unittest.TestCase):
    """Tests for `timeConversion.py`."""

    def test_testcase_0(self):
        """Midnight"""
        self.assertTrue(timeConversion._12to24("12:00:00AM") == "00:00:00")

    def test_testcase_1(self):
        """One second after midnight"""
        self.assertTrue(timeConversion._12to24("12:00:01AM") == "00:00:01")

    def test_testcase_2(self):
        """One O'Clock"""
        self.assertTrue(timeConversion._12to24("01:00:00AM") == "01:00:00")

    def test_testcase_3(self):
        """Noon"""
        self.assertTrue(timeConversion._12to24("12:00:00PM") == "12:00:00")

    def test_testcase_4(self):
        """One second after noon"""
        self.assertTrue(timeConversion._12to24("12:00:01PM") == "12:00:01")

    def test_testcase_5(self):
        """One O'Clock after noon"""
        self.assertTrue(timeConversion._12to24("01:00:00PM") == "13:00:00")

if __name__ == '__main__':
    unittest.main()