from unittest import TestCase

from day12.rr1.directions import *


class TestNorth(TestCase):
    def test_move(self):
        self.assertTupleEqual((0,-5),North.move((0,0),5))

    def test_move_left_90(self):
        self.assertEqual(type(West),type(North.move_left(90)))

    def test_move_left_270(self):
        self.assertEqual(type(East),type(North.move_left(270)))

    def test_move_left_450(self):
        self.assertEqual(type(West),type(North.move_left(450)))

    def test_move_right_90(self):
        self.assertEqual(type(East),type(North.move_right(90)))
        
    def test_move_right_270(self):
        self.assertEqual(type(West),type(North.move_right(270)))
        
    def test_move_right_450(self):
        self.assertEqual(type(East),type(North.move_right(450)))


class TestEast(TestCase):
    def test_move(self):
        self.assertTupleEqual((5, 0), East.move((0, 0), 5))

    def test_move_left_90(self):
        self.assertEqual(type(North), type(East.move_left(90)))

    def test_move_left_270(self):
        self.assertEqual(type(South), type(East.move_left(270)))

    def test_move_left_450(self):
        self.assertEqual(type(North), type(East.move_left(450)))

    def test_move_right_90(self):
        self.assertEqual(type(South), type(East.move_right(90)))

    def test_move_right_270(self):
        self.assertEqual(type(North), type(East.move_right(270)))

    def test_move_right_450(self):
        self.assertEqual(type(South), type(East.move_right(450)))


class TestSouth(TestCase):
    def test_move(self):
        self.assertTupleEqual((0, 5), South.move((0, 0), 5))

    def test_move_left_90(self):
        self.assertEqual(type(East), type(South.move_left(90)))

    def test_move_left_270(self):
        self.assertEqual(type(West), type(South.move_left(270)))

    def test_move_left_450(self):
        self.assertEqual(type(East), type(South.move_left(450)))

    def test_move_right_90(self):
        self.assertEqual(type(West), type(South.move_right(90)))

    def test_move_right_270(self):
        self.assertEqual(type(East), type(South.move_right(270)))

    def test_move_right_450(self):
        self.assertEqual(type(West), type(South.move_right(450)))


class TestWest(TestCase):
    def test_move(self):
        self.assertTupleEqual((-5, 0), West.move((0, 0), 5))

    def test_move_left_90(self):
        self.assertEqual(type(South), type(West.move_left(90)))

    def test_move_left_270(self):
        self.assertEqual(type(North), type(West.move_left(270)))

    def test_move_left_450(self):
        self.assertEqual(type(South), type(West.move_left(450)))

    def test_move_right_90(self):
        self.assertEqual(type(North), type(West.move_right(90)))

    def test_move_right_270(self):
        self.assertEqual(type(South), type(West.move_right(270)))

    def test_move_right_450(self):
        self.assertEqual(type(North), type(West.move_right(450)))