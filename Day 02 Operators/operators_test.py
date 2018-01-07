import unittest
import sys
from io import StringIO

import operators

class OperatorsTestCase(unittest.TestCase):

    def test_testcase_0(self):

        temp_stdout = sys.stdout
        sys.stdout = output = StringIO()

        sys.stdin.close()
        sys.stdin = open('testcase_0_input', 'r')

        # your code here
        print("The total meal cost is " + operators.get_total_cost_of_meal() + " dollars.")

        sys.stdout = temp_stdout
        output = output.getvalue().strip()
        with open('testcase_0_output', 'r') as f:
            expected = f.read()
        f.closed
        
        self.assertTrue(output == expected)


    def test_testcase_1(self):

        temp_stdout = sys.stdout
        sys.stdout = output = StringIO()

        sys.stdin.close()
        sys.stdin = open('testcase_1_input', 'r')

        # your code here
        print("The total meal cost is " + operators.get_total_cost_of_meal() + " dollars.")

        sys.stdout = temp_stdout
        output = output.getvalue().strip()
        with open('testcase_1_output', 'r') as f:
            expected = f.read()
        f.closed
        
        self.assertTrue(output == expected)


if __name__ == '__main__':
    unittest.main()