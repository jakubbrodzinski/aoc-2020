from day12.rr1.directions import *


class RainRisk:
    def __init__(self, instructions: [str]):
        self._direction = East
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
            self._position = North.move(self._position, value)
        elif command == 'S':
            self._position = South.move(self._position, value)
        elif command == 'E':
            self._position = East.move(self._position, value)
        elif command == 'W':
            self._position = West.move(self._position, value)
        elif command == 'L':
            self._direction = self._direction.move_left(value)
        elif command == 'R':
            self._direction = self._direction.move_right(value)
        elif command == 'F':
            self._position = self._direction.move_forward(self._position, value)

    @staticmethod
    def get_manhattan_distance(position: (int,int)) -> int:
        return abs(position[0]) + abs(position[1])
