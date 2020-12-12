class TobogganMap:
    __tree_char = '#'

    def __init__(self, input: [str]):
        self.__map_width = len(input[0])
        self.__height = len(input)

        self.__map = []
        for row in input:
            self.__map.append(self.__parse_row(row))

    def __parse_row(self, row: str) -> [str]:
        map_row = []
        for cell in row:
            if cell == self.__tree_char:
                map_row.append(True)
            else:
                map_row.append(False)
        return map_row

    def get_height(self) -> int:
        return self.__height

    def has_tree(self, x: int, y: int) -> bool:
        return self.__map[y - 1][(x - 1) % self.__map_width]


class TobogganTrajectory:
    def __init__(self, map: TobogganMap):
        self.__map = map

    def count_collisions(self, x_step=3, y_step=1) -> int:
        collisions_counter = 0
        x_position = 1
        for y_position in range(1, self.__map.get_height() + 1,y_step):
            if self.__map.has_tree(x_position, y_position):
                collisions_counter += 1
            x_position += x_step
        return collisions_counter
