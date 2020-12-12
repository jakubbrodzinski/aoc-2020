from unittest import TestCase
from day5.BinaryBoarding import BinaryBoardingParser

class TestBinaryBoardingParser(TestCase):
    def test_parse(self):
        self.assertEqual(567,BinaryBoardingParser.parse('BFFFBBFRRR'))

    def test_parse_2(self):
        self.assertEqual(119, BinaryBoardingParser.parse('FFFBBBFRRR'))

    def test_parse_3(self):
        self.assertEqual(820, BinaryBoardingParser.parse('BBFFBBFRLL'))

    def test_parse_4(self):
        self.assertEqual(357,BinaryBoardingParser.parse('FBFBBFFRLR'))
