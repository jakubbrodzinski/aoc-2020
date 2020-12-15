from unittest import TestCase

from day14.docking_data import BitmapSystem, BitmapSystem2


class TestBitmapSystem(TestCase):
    def test_proccess(self):
        bs = BitmapSystem('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
        self.assertEqual(73, bs.proccess(11))

    def test_proccess_2(self):
        bs = BitmapSystem('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
        self.assertEqual(101, bs.proccess(101))

    def test_proccess_3(self):
        bs = BitmapSystem('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
        self.assertEqual(64, bs.proccess(0))


class TestBitmapSystem2(TestCase):
    def test_proccess(self):
        bs = BitmapSystem2('000000000000000000000000000000X1001X')
        self.assertListEqual([26,27,58,59], bs.process('42'))
