import unittest
import sys
from io import StringIO

from dataTypes import dataTypes

class DataTypesTestCase(unittest.TestCase):

    def test_testcase_0(self):

        temp_stdout = sys.stdout
        sys.stdout = output = StringIO()

        sys.stdin.close()
        sys.stdin = open('testcase_0_input', 'r')

        # your code here
        dataTypes()

        sys.stdout = temp_stdout
        output = output.getvalue().strip()
        with open('testcase_0_output', 'r') as f:
            expected = f.read()
        f.closed
        
        self.assertTrue(output == expected)


if __name__ == '__main__':
    unittest.main()