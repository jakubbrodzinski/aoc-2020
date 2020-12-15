from unittest import TestCase

from day12.rr1.rain_risk import RainRisk
from utils.file_utils import read_file_lines


class TestRainRisk(TestCase):
    def test_follow_instructions(self):
        rr = RainRisk(read_file_lines('../input/test-data'))
        self.assertTupleEqual((17, 8), rr.follow_instructions())

    def test_get_manhattan_distance(self):
        self.assertEqual(25, RainRisk.get_manhattan_distance((17,8)))

    def test_get_manhattan_distance_2(self):
        self.assertEqual(25, RainRisk.get_manhattan_distance((-17,-8)))
