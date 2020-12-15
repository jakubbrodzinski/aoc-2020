class Waypoint:
    def __init__(self, init_value: (int, int) = (0, 0)):
        self._value = init_value

    def move_north(self, value: int):
        return Waypoint((self._value[0], self._value[1] - value))

    def move_east(self, value: int):
        return Waypoint((self._value[0] + value, self._value[1]))

    def move_south(self, value: int):
        return Waypoint((self._value[0], self._value[1] + value))

    def move_west(self, value: int):
        return Waypoint((self._value[0] - value, self._value[1]))

    def rotate_r(self, value: int):
        return self.__rotate((value // 90) % 4)

    def rotate_l(self, value: int):
        return self.__rotate(4 - (value // 90) % 4)

    def __rotate(self, value: int):
        if value == 1:
            return Waypoint((-self._value[1], self._value[0]))
        elif value == 2:
            return Waypoint((-self._value[0], -self._value[1]))
        elif value == 3:
            return Waypoint((self._value[1], -self._value[0]))

    def move(self, position: (int, int), value: int) -> (int, int):
        move_x = self._value[0] * value
        move_y = self._value[1] * value

        return position[0] + move_x, position[1] + move_y
