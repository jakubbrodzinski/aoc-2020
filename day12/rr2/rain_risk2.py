from day12.rr2.waypoint import Waypoint


class RainRisk2:
    def __init__(self, instructions: [str]):
        self._waypoint = Waypoint((10, -1))
        self._position = (0, 0)
        self._instructions = instructions

    def follow_instructions(self) -> (int, int):
        for instruction in self._instructions:
            self.__follow_instruction(instruction)

        return self._position

    def __follow_instruction(self, instruction: str):
        command = instruction[0]
        value = int(instruction[1:])
        if command == 'N':
            self._waypoint = self._waypoint.move_north(value)
        elif command == 'S':
            self._waypoint = self._waypoint.move_south(value)
        elif command == 'E':
            self._waypoint = self._waypoint.move_east(value)
        elif command == 'W':
            self._waypoint = self._waypoint.move_west(value)
        elif command == 'L':
            self._waypoint = self._waypoint.rotate_l(value)
        elif command == 'R':
            self._waypoint = self._waypoint.rotate_r(value)
        elif command == 'F':
            self._position = self._waypoint.move(self._position, value)

    @staticmethod
    def get_manhattan_distance(position: (int, int)) -> int:
        return abs(position[0]) + abs(position[1])
