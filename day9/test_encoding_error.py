from unittest import TestCase
from day9.encoding_error import EncodingError
from utils.file_utils import read_file_lines_as_ints


class TestEncodingError(TestCase):
    def test_find_numbers_with_sum_equal(self):
        self.assertTrue(EncodingError.exist_numbers_with_sum_equal([1, 2, 3, 4], 5))

    def test_find_numbers_with_sum_equal_2(self):
        self.assertFalse(EncodingError.exist_numbers_with_sum_equal([1, 2, 3, 4], 8))

    def test_find_invalid_entry(self):
        ee = EncodingError(read_file_lines_as_ints('input/test-data'),5)
        self.assertEqual(ee.find_invalid_entry(),127)

    def test_find_invalid_entry_2(self):
        ee = EncodingError(read_file_lines_as_ints('input/input-data'),25)
        self.assertEqual(ee.find_invalid_entry(),32321523)

    def test_find_contiguous_set_that_sums_to_invalid_entry(self):
        ee = EncodingError(read_file_lines_as_ints('input/test-data'), 5)
        self.assertListEqual(sorted(ee.find_contiguous_set_that_sums_to_invalid_entry()),[15,25,40,47])
