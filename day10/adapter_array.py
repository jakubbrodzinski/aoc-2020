class AdapterArray:
    def __init__(self, adapters_list: [int]):
        adapters_list.append(0)
        self.__adapters = sorted(adapters_list)
        self.__adapters.append(self.__adapters[-1] + 3)

    def get_diffs_tuple(self) -> (int, int, int):
        diffs = [0, 0, 0]
        for i in range(0, len(self.__adapters) - 1):
            diff = self.__adapters[i + 1] - self.__adapters[i]
            diffs[diff - 1] += 1

        return diffs[0], diffs[1], diffs[2]

    def count_possible_connections(self) -> int:
        # return self._count_possible_connections_from_pos(0)
        diffs = self.__count_diffs()
        diffs[0] = 3
        pos = AdapterArray.__find_next_diff_not_eq_3(diffs, 0)
        combination_counter = 1
        while pos != -1:
            left = pos - 1
            right = AdapterArray.__find_next_diff_eq_3(diffs, pos)
            combination_counter *= AdapterArray.count_combinations(diffs[left:right + 1])

            pos = AdapterArray.__find_next_diff_not_eq_3(diffs, right)

        return combination_counter

    @staticmethod
    def __find_next_diff_eq_3(diffs, start) -> int:  # last elt of diffs is always 3
        for i in range(start, len(diffs)):
            if diffs[i] == 3:
                return i

    @staticmethod
    def __find_next_diff_not_eq_3(diffs: [int], start: int) -> int:
        for i in range(start, len(diffs)):
            if diffs[i] != 3:
                return i
        return -1

    def __count_diffs(self):
        diffs = [0]
        for i in range(1, len(self.__adapters)):
            diffs.append(self.__adapters[i] - self.__adapters[i - 1])
        return diffs

    @staticmethod
    def count_combinations(slice: [int]):
        return AdapterArray.__count_combinations_from_pos(slice, 0)

    @staticmethod
    def __count_combinations_from_pos(sliced_diffs: [int], start_pos: int) -> int:
        if start_pos + 1 == len(sliced_diffs):
            return 1

        jump_pos = start_pos + 1
        jump_cost = sliced_diffs[jump_pos]
        count = 0

        while jump_cost < 4:
            count += AdapterArray.__count_combinations_from_pos(sliced_diffs, jump_pos)

            jump_pos += 1
            if jump_pos == len(sliced_diffs):
                return count

            jump_cost += sliced_diffs[jump_pos]

        return count
