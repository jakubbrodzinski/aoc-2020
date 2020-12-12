from day11.seating_system import SeatingSystem


class SeatingSystem2(SeatingSystem):
    def __init__(self, grid: [str]):
        super().__init__(grid)
        self.__init_cached_seats()

    def __init_cached_seats(self):
        self.__cached_visible_seats = []
        for i in range(0, self._height):
            row = []
            for j in range(0, self._width):
                row.append(self.__get_visible_seats_list(i, j))
            self.__cached_visible_seats.append(row)

    def proceed_next_round(self):
        occupied_seats_counts = self.__count_occupied_seats_for_next_round()
        for i in range(0, self._height):
            for j in range(0, self._width):
                occupied_seats_counts[i][j] = self.__get_seat_new_state(self._grid[i][j], occupied_seats_counts[i][j])

        return occupied_seats_counts

    def __count_occupied_seats_for_next_round(self):
        occupied_seats_counts = []
        for i in range(0, self._height):
            row = []
            for j in range(0, self._width):
                o_c = 0
                for visible_seat in self.__cached_visible_seats[i][j]:
                    if self.__is_seat_occupied(self._grid[visible_seat[0]][visible_seat[1]]):
                        o_c += 1
                row.append(o_c)
            occupied_seats_counts.append(row)
        return occupied_seats_counts

    def __get_visible_seats_list(self, row, col) -> [(int, int)]:
        if not self.__is_seat(self._grid[row][col]):
            return []

        return list(filter(lambda x: x is not None, [
            self.__find_visible_seat_to_left(row, col),
            self.__find_visible_seat_to_lt(row, col),
            self.__find_visible_seat_to_top(row, col),
            self.__find_visible_seat_to_rt(row, col),
            self.__find_visible_seat_to_right(row, col),
            self.__find_visible_seat_to_rb(row, col),
            self.__find_visible_seat_to_bottom(row, col),
            self.__find_visible_seat_to_lb(row, col)
        ]))

    def __find_visible_seat_to_left(self, row, start_col):
        col = start_col - 1
        while not col < 0:
            if self.__is_seat(self._grid[row][col]):
                return row, col
            col -= 1
        return None

    def __find_visible_seat_to_right(self, row, start_col):
        col = start_col + 1
        while col < self._width:
            if self.__is_seat(self._grid[row][col]):
                return row, col
            col += 1
        return None

    def __find_visible_seat_to_bottom(self, start_row, col):
        row = start_row - 1
        while not row < 0:
            if self.__is_seat((self._grid[row][col])):
                return row, col
            row -= 1
        return None

    def __find_visible_seat_to_top(self, start_row, col):
        row = start_row + 1
        while row < self._height:
            if self.__is_seat((self._grid[row][col])):
                return row, col
            row += 1
        return None

    def __find_visible_seat_to_lt(self, start_row, start_col):
        row = start_row - 1
        col = start_col - 1
        while not row < 0 and not col < 0:
            if self.__is_seat((self._grid[row][col])):
                return row, col
            row -= 1
            col -= 1
        return None

    def __find_visible_seat_to_rb(self, start_row, start_col):
        row = start_row + 1
        col = start_col + 1
        while row < self._height and col < self._width:
            if self.__is_seat((self._grid[row][col])):
                return row, col
            row += 1
            col += 1
        return None

    def __find_visible_seat_to_rt(self, start_row, start_col):
        row = start_row + 1
        col = start_col - 1
        while row < self._height and not col < 0:
            if self.__is_seat((self._grid[row][col])):
                return row, col
            row += 1
            col -= 1
        return None

    def __find_visible_seat_to_lb(self, start_row, start_col):
        row = start_row - 1
        col = start_col + 1
        while not row < 0 and col < self._width:
            if self.__is_seat((self._grid[row][col])):
                return row, col
            row -= 1
            col += 1
        return None

    @staticmethod
    def __is_seat(seat) -> bool:
        return seat != '.'

    @staticmethod
    def __is_seat_occupied(seat) -> bool:
        return seat == '#'

    @staticmethod
    def __get_seat_new_state(old_state, occupied_count):
        if old_state == 'L' and occupied_count == 0:
            return '#'
        elif old_state == '#' and occupied_count >= 5:
            return 'L'
        else:
            return old_state
