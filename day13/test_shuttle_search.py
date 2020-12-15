from unittest import TestCase

from utils.file_utils import read_file_lines
from day13.shuttle_search import ShuttleSearch


class TestShuttleSearch(TestCase):
    def test_get_earliest_connection(self):
        input = read_file_lines('input/test-data')
        ss = ShuttleSearch(input[0], input[1])
        self.assertEqual((59, 944), ss.get_earliest_connection())

    def test_calculate_output(self):
        input = read_file_lines('input/test-data')
        ss = ShuttleSearch(input[0], input[1])
        self.assertEqual(295, ss.calculate_output(59, 944))

    def test_get_timestamp_with_constraints(self):
        ss = ShuttleSearch('0', '67,7,59,61')
        self.assertEqual(754018, ss.get_timestamp_with_constraints())

    def test_get_timestamp_with_constraints_2(self):
        ss = ShuttleSearch('0', '67,x,7,59,61')
        self.assertEqual(779210, ss.get_timestamp_with_constraints())

    def test_get_timestamp_with_constraints_3(self):
        ss = ShuttleSearch('0', '67,7,x,59,61')
        self.assertEqual(1202161486, ss.get_timestamp_with_constraints())

    def test_get_timestamp_with_constraints_5(self):
        ss = ShuttleSearch('0', '17,x,13,19')
        self.assertEqual(3417, ss.get_timestamp_with_constraints())

    def test_get_timestamp_with_constraints_6(self):
        ss = ShuttleSearch('0', '7,13,x,x,59,x,31,19')
        self.assertEqual(1068781, ss.get_timestamp_with_constraints())
    #
    # def test_get_timestamp_with_constraints_4(self):
    #     ss = ShuttleSearch('0', '1789,37,47,1889')
    #     self.assertEqual(1202161486, ss.get_timestamp_with_constraints())