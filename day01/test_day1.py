import unittest

from day01.day1 import get_max, split_input, sum_groups, sum_top_x

#from .day1 import split_input, sum_groups, get_max, sum_top_x


class TestSum(unittest.TestCase):

    def test_split_input(self):
        self.assertEqual(split_input("1\n2\n3\n\n4\n5\n6\n\n7\n8\n9"), [
                         "1\n2\n3", "4\n5\n6", "7\n8\n9"])

    def test_sum_groups(self):
        self.assertEqual(sum_groups(
            ["1\n2\n3", "4\n5\n6", "7\n8\n9"]), [6, 15, 24])

    def test_get_max(self):
        self.assertEqual(get_max([6, 15, 24]), 24)

    def test_sum_top_x(self):
        self.assertEqual(sum_top_x([6, 15, 24], 2), 39)


if __name__ == "__main__":
    unittest.main()
