from unittest import TestCase

from day3.toboggan_trajectory import TobogganMap, TobogganTrajectory
from utils.file_utils import read_file_lines


class TestTobogganMap(TestCase):
    def test_get_height(self):
        map = TobogganMap(["..##.......", "..##......."])
        self.assertEqual(map.get_height(), 2)

    def test_has_tree(self):
        map = TobogganMap(["..##.......", ])
        self.__assert_row(map, [3, 4], [1, 2, 5, 6, 7, 8, 9, 10, 11], 1)

    def test_has_tree_extending_map(self):
        map = TobogganMap(["..##.......", ])
        self.__assert_row(map, [14, 15], [12, 13, 16, 17, 18, 19, 20, 21, 22], 1)

    def __assert_row(self, map: TobogganMap, tree_positions, empty_positions, row_num):
        for tree in tree_positions:
            self.assertTrue(map.has_tree(tree, row_num))
        for empty_position in empty_positions:
            self.assertFalse(map.has_tree(empty_position, row_num))


class TestTobogganTrajectory(TestCase):
    def test_count_collisions(self):
        self.assert_collisions_amount(3,7)

    def test_count_collisions_step_1(self):
        self.assert_collisions_amount(1,2)

    def test_count_collisions_step_5(self):
        self.assert_collisions_amount(5,3)

    def test_count_collisions_step_7(self):
        self.assert_collisions_amount(7,4)

    def test_count_collisions_different_both_steps(self):
        self.assert_collisions_amount_with_two_custom_steps(1,2,2)

    def assert_collisions_amount(self, x_step, expected_amount):
        trajectory = self.__get_test_trajectory()
        self.assertEqual(trajectory.count_collisions(x_step), expected_amount)

    def assert_collisions_amount_with_two_custom_steps(self, x_step, y_step, expected_amount):
        trajectory = self.__get_test_trajectory()
        self.assertEqual(trajectory.count_collisions(x_step,y_step), expected_amount)

    def __get_test_trajectory(self):
        test_input = read_file_lines('input/test-data')
        map = TobogganMap(test_input)
        return TobogganTrajectory(map)
