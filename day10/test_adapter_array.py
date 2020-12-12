from unittest import TestCase

from day10.adapter_array import AdapterArray
from utils.file_utils import read_file_lines_as_ints


class TestAdapterArray(TestCase):
    def test_get_diffs_tuple(self):
        aa = AdapterArray(read_file_lines_as_ints('input/test-data'))
        self.assertTupleEqual((7, 0, 5), aa.get_diffs_tuple())

    def test_get_diffs_tuple_2(self):
        aa = AdapterArray(read_file_lines_as_ints('input/test-data-2'))
        self.assertTupleEqual((22, 0, 10), aa.get_diffs_tuple())

    def test__count_possible_connections(self):
        aa = AdapterArray(read_file_lines_as_ints('input/test-data'))
        self.assertEqual(8, aa.count_possible_connections())

    def test__count_possible_connections_2(self):
        aa = AdapterArray(read_file_lines_as_ints('input/test-data-2'))
        self.assertEqual(19208, aa.count_possible_connections())

    def test__count_possible_connections_3(self):
        aa = AdapterArray(read_file_lines_as_ints('input/input-data'))
        self.assertEqual(4049565169664, aa.count_possible_connections())

    def test_count_combination(self):
        self.assertEqual(4, AdapterArray.count_combinations([3, 1, 1, 1, 3]))

    def test_count_combination_2(self):
        self.assertEqual(2, AdapterArray.count_combinations([3, 1, 1, 3]))

    def test_count_combination_3(self):
        self.assertEqual(13, AdapterArray.count_combinations([3, 1, 1, 1, 1, 1, 3]))
