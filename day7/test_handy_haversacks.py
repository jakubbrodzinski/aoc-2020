from unittest import TestCase
from utils.file_utils import read_file_lines
from day7.handy_haversacks import HandyHaversacks,HandyHaversacks2


class TestHandyHaversacks(TestCase):
    def test_count_valid_outermost_bags(self):
        test_input = read_file_lines('input/test-data')
        hh = HandyHaversacks(test_input)
        self.assertEqual(hh.count_valid_outermost_bags('shiny gold'), 4)


class TestHandyHaversacks2(TestCase):
    def test_count_inner_bags(self):
        test_input = read_file_lines('input/test-data')
        hh2 = HandyHaversacks2(test_input)
        self.assertEqual(hh2.count_inner_bags('shiny gold'), 32)

    def test_count_inner_bags_2(self):
        test_input = read_file_lines('input/test-data-2')
        hh2 = HandyHaversacks2(test_input)
        self.assertEqual(hh2.count_inner_bags('shiny gold'), 126)