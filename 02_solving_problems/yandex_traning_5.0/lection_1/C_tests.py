import unittest
from io import StringIO
import sys
import C

def calculate_result(input_values):
    result = 0
    sys.stdin = StringIO(input_values)
    for i in range(int(input())):
        number = int(input())
        result += number // 4
        if (number % 4 == 1):
            result += 1
        elif (number % 4 == 0):
            continue
        else:
            result += 2
    return result

class TestCode(unittest.TestCase):
    def test_example(self):
        input_values = '3\n5\n8\n9\n'
        expected_output = '6\n'
        actual_output = StringIO()
        sys.stdout = actual_output
        calculate_result(input_values)
        sys.stdout = sys.__stdout__
        self.assertEqual(actual_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()