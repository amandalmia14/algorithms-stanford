import unittest
from unittest.mock import patch

from part_1.assignment_6_1_2sum.app.two_sum_finder import TwoSumFinder


class TestTwoSumFinder(unittest.TestCase):
    @patch('builtins.input', return_value='1 4 45 6 10 10 8')
    def test_find_2sum_pairs_test1_forum(self, stdin):
        two_sum_finder = TwoSumFinder()
        expected_values = 14
        self.assertEqual(two_sum_finder.compute_values(), expected_values)

if __name__ == '__main__':
    unittest.main()