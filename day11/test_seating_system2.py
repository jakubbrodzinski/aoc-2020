from unittest import TestCase

from day11.seating_system2 import SeatingSystem2
from utils.file_utils import read_file_lines


class TestSeatingSystem2(TestCase):
    def test_proceed_first_round(self):
        ss = SeatingSystem2(read_file_lines('input/test-data'))
        self.assertListEqual([
            ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
            ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
            ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#']
        ], ss.proceed_next_round())

    def test_proceed_second_round(self):
        ss = SeatingSystem2(read_file_lines('input/test-data'))
        ss.proceed_and_save_next_round()
        self.assertListEqual([
            ['#', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', '#'],
            ['#', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
            ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'],
            ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
            ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
            ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
            ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '#'],
            ['#', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'],
            ['#', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', '#']
        ], ss.proceed_next_round())

    def test_proceed_third_round(self):
        ss = SeatingSystem2(read_file_lines('input/test-data'))
        ss.proceed_and_save_next_round()
        ss.proceed_and_save_next_round()
        self.assertListEqual([
            ['#', '.', 'L', '#', '.', '#', '#', '.', 'L', '#'],
            ['#', 'L', '#', '#', '#', '#', '#', '.', 'L', 'L'],
            ['L', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
            ['#', '#', 'L', '#', '.', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '#', '.', '#', 'L', '.', '#', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '.', '#', 'L'],
            ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
            ['L', 'L', 'L', '#', '#', '#', '#', 'L', 'L', '#'],
            ['#', '.', 'L', '#', '#', '#', '#', '#', '.', 'L'],
            ['#', '.', 'L', '#', '#', '#', '#', '.', 'L', '#']
        ], ss.proceed_next_round())

    def test_proceed_fourth_round(self):
        ss = SeatingSystem2(read_file_lines('input/test-data'))
        ss.proceed_and_save_next_round()
        ss.proceed_and_save_next_round()
        ss.proceed_and_save_next_round()
        self.assertListEqual([
            ['#', '.', 'L', '#', '.', 'L', '#', '.', 'L', '#'],
            ['#', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
            ['L', '.', 'L', '.', 'L', '.', '.', '#', '.', '.'],
            ['#', '#', 'L', 'L', '.', 'L', 'L', '.', 'L', '#'],
            ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', '#'],
            ['#', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
            ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '#'],
            ['#', '.', 'L', 'L', 'L', 'L', 'L', '#', '.', 'L'],
            ['#', '.', 'L', '#', 'L', 'L', '#', '.', 'L', '#']
        ], ss.proceed_next_round())

    def test_proceed_fifth_round(self):
        ss = SeatingSystem2(read_file_lines('input/test-data'))
        ss.proceed_and_save_next_round()
        ss.proceed_and_save_next_round()
        ss.proceed_and_save_next_round()
        ss.proceed_and_save_next_round()
        self.assertListEqual([
            ['#', '.', 'L', '#', '.', 'L', '#', '.', 'L', '#'],
            ['#', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
            ['L', '.', 'L', '.', 'L', '.', '.', '#', '.', '.'],
            ['#', '#', 'L', '#', '.', '#', 'L', '.', 'L', '#'],
            ['L', '.', 'L', '#', '.', '#', 'L', '.', 'L', '#'],
            ['#', '.', 'L', '#', '#', '#', '#', '.', 'L', 'L'],
            ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
            ['L', 'L', 'L', '#', '#', '#', 'L', 'L', 'L', '#'],
            ['#', '.', 'L', 'L', 'L', 'L', 'L', '#', '.', 'L'],
            ['#', '.', 'L', '#', 'L', 'L', '#', '.', 'L', '#']
        ], ss.proceed_next_round())


    def test_get_round_amount_before_stabilization(self):
        ss = SeatingSystem2(read_file_lines('input/test-data'))
        self.assertEqual(26, ss.get_occupied_seats_count_after_stabilization())
