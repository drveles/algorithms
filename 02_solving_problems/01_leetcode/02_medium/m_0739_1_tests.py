from m_0739_1 import Solution 
import unittest


class TestSolution(unittest.TestCase):
    def test_dailyTemperatures(self):
        solution = Solution()
        
        # Тест на пустой входной список
        self.assertEqual(solution.dailyTemperatures([]), [])
        
        # Тест на входной список из одного элемента
        self.assertEqual(solution.dailyTemperatures([10]), [0])
        
        # Тест на обычный случай
        self.assertEqual(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])

        # Тест на входной список, где все значения температуры равны
        self.assertEqual(solution.dailyTemperatures([50, 50, 50, 50, 50]), [0, 0, 0, 0, 0])

        # Тест на входной список, где температуры убывают
        self.assertEqual(solution.dailyTemperatures([50, 40, 30, 20, 10]), [0, 0, 0, 0, 0])

        # Тест на входной список, где температуры возрастают
        self.assertEqual(solution.dailyTemperatures([10, 20, 30, 40, 50]), [1, 1, 1, 1, 0])

        self.assertEqual(solution.dailyTemperatures([30, 20, 30, 40, 50]), [3, 1, 1, 1, 0])

if __name__ == '__main__':
    unittest.main()