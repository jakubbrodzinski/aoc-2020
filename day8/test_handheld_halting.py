from unittest import TestCase

from day8.handheld_halting import HandheldHalting
from utils.file_utils import read_file_lines


class TestHandheldHalting(TestCase):
    def test_get_acc_value_before_looped(self):
        hh = HandheldHalting(read_file_lines('input/test-data'))
        self.assertEqual(hh.get_acc_value_before_looped(), 5)

    def test_get_acc_value_with_changed_single_command(self):
        hh = HandheldHalting(read_file_lines('input/test-data'))
        self.assertEqual(hh.get_acc_value_with_changed_single_command(),8)
