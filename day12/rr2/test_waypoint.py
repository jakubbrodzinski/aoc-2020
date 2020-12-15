from unittest import TestCase

from day12.rr2.waypoint import Waypoint


class TestWaypoint(TestCase):
    def test_move_north(self):
        self.assertEqual((0, -15), Waypoint()
                         .move_north(5)
                         .move((0, 0), 3)
                         )

    def test_move_east(self):
        self.assertEqual((15, 0), Waypoint()
                         .move_east(5)
                         .move((0, 0), 3)
                         )

    def test_move_south(self):
        self.assertEqual((0, 15), Waypoint()
                         .move_south(5)
                         .move((0, 0), 3)
                         )

    def test_move_west(self):
        self.assertEqual((-15, 0), Waypoint()
                         .move_west(5)
                         .move((0, 0), 3)
                         )

    def test_rotate_r_90(self):
        self.assertEqual((-2, 3), Waypoint((3, 2))
                         .rotate_r(90)
                         .move((0, 0), 1)
                         )

    def test_rotate_r_180(self):
        self.assertEqual((-3, -2), Waypoint((3, 2))
                         .rotate_r(180)
                         .move((0, 0), 1)
                         )

    def test_rotate_r_270(self):
        self.assertEqual((2, -3), Waypoint((3, 2))
                         .rotate_r(270)
                         .move((0, 0), 1)
                         )

    def test_rotate_l_90(self):
        self.assertEqual((2, -3), Waypoint((3, 2))
                         .rotate_l(90)
                         .move((0, 0), 1)
                         )

    def test_rotate_l_180(self):
        self.assertEqual((-3, -2), Waypoint((3, 2))
                         .rotate_l(180)
                         .move((0, 0), 1)
                         )

    def test_rotate_l_270(self):
        self.assertEqual((-2, 3), Waypoint((3, 2))
                         .rotate_l(270)
                         .move((0, 0), 1)
                         )
