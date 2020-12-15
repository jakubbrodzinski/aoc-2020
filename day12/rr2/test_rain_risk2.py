from unittest import TestCase

from day12.rr2.rain_risk2 import RainRisk2
from utils.file_utils import read_file_lines

class TestRainRisk2(TestCase):
    def test_follow_instructions(self):
        rr2 = RainRisk2(read_file_lines('../input/test-data'))
        self.assertTupleEqual((214, 72), rr2.follow_instructions())
