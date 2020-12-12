class SeatingSystem:
    def __init__(self, grid: [str]):
        self._grid = []
        for input_row in grid:
            row = []
            for seat in input_row:
                row.append(seat)
            self._grid.append(row)
        self._width = len(grid[0])
        self._height = len(grid)

    def get_occupied_seats_count_after_stabilization(self):
        new_grid = self.proceed_next_round()
        round_counter = 0
        while self.__has_changed(self._grid, new_grid):
            self._grid = new_grid
            new_grid = self.proceed_next_round()
            round_counter += 1
        self._grid = new_grid

        print("rounds: " + str(round_counter))

        seats_counter = 0
        for i in range(0, self._height):
            for j in range(0, self._width):
                seats_counter += self.__check_seat(self._grid[i][j])

        return seats_counter

    @staticmethod
    def __has_changed(old_grid, new_grid):
        for i in range(0, len(old_grid)):
            for j in range(0, len(new_grid)):
                if old_grid[i][j] != new_grid[i][j]:
                    return True
        return False

    def proceed_next_round(self) -> [[str]]:
        occupied_seats_counts = self.__count_occupied_seats_for_next_round()
        for i in range(0, self._height):
            for j in range(0, self._width):
                occupied_seats_counts[i][j] = self.__get_seat_new_state(self._grid[i][j], occupied_seats_counts[i][j])

        return occupied_seats_counts

    def proceed_and_save_next_round(self):
        self._grid = self.proceed_next_round()

    def __count_occupied_seats_for_next_round(self):
        occupied_seats_counts = []

        row = [0] * self._width
        self.__add_same_row(row, 0)
        self.__add_row_below(row, 0)
        occupied_seats_counts.append(row)

        for i in range(1, self._height - 1):
            row = [0] * self._width
            self.__add_row_above(row, i)
            self.__add_same_row(row, i)
            self.__add_row_below(row, i)

            occupied_seats_counts.append(row)

        row = [0] * self._width
        self.__add_same_row(row, self._height - 1)
        self.__add_row_above(row, self._height - 1)
        occupied_seats_counts.append(row)

        return occupied_seats_counts

    def __add_row_below(self, row, row_num):
        row_below = self._grid[row_num + 1]
        first_down = self.__check_seat(row_below[0])
        row[0] += first_down
        row[1] += first_down

        last_down = self.__check_seat(row_below[-1])
        row[-1] += last_down
        row[-2] += last_down

        for i in range(1, self._width - 1):
            one_down = self.__check_seat(row_below[i])
            row[i - 1] += one_down
            row[i] += one_down
            row[i + 1] += one_down

    def __add_same_row(self, row, row_num):
        same_row = self._grid[row_num]
        row[1] += self.__check_seat(same_row[0])
        row[-2] += self.__check_seat(same_row[-1])

        for i in range(1, self._width - 1):
            val = self.__check_seat(same_row[i])
            row[i - 1] += val
            row[i + 1] += val

    def __add_row_above(self, row, row_num):
        row_up = self._grid[row_num - 1]

        first_up = self.__check_seat(row_up[0])
        row[0] += first_up
        row[1] += first_up

        last_up = self.__check_seat(row_up[-1])
        row[-1] += last_up
        row[-2] += last_up

        for i in range(1, self._width - 1):
            one_up = self.__check_seat(row_up[i])
            row[i - 1] += one_up
            row[i] += one_up
            row[i + 1] += one_up

    @staticmethod
    def __check_seat(seat) -> int:
        return 1 if seat == '#' else 0

    @staticmethod
    def __is_seat_empty(seat) -> bool:
        return seat == 'L'

    @staticmethod
    def __is_seat_occupied(seat) -> bool:
        return seat == '#'

    @staticmethod
    def __get_seat_new_state(old_state, occupied_count):
        if old_state == 'L' and occupied_count == 0:
            return '#'
        elif old_state == '#' and occupied_count >= 4:
            return 'L'
        else:
            return old_state
