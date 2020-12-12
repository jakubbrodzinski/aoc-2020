from unittest import TestCase

from day6.custom_customs import CustomCustoms
from utils.file_utils import read_file_lines


class TestCustomCustoms(TestCase):
    def test_count_all_valid_answers(self):
        test_input = read_file_lines('input/test-data')
        self.assertEqual(CustomCustoms.count_all_valid_answers(test_input),11)

    def test_count_always_valid_answers(self):
        test_input = read_file_lines('input/test-data')
        self.assertEqual(CustomCustoms.count_always_valid_answers(test_input), 6)