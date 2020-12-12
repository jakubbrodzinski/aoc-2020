class EncodingError:
    def __init__(self, entries: [int], preamble_len: int):
        self.__preamble_len = preamble_len
        self.__entries = entries

    def find_invalid_entry(self):
        preamble = sorted(self.__entries[0: self.__preamble_len])
        for i in range(self.__preamble_len, len(self.__entries)):
            first_number = self.__entries[i - self.__preamble_len]
            next_number = self.__entries[i]
            if not EncodingError.exist_numbers_with_sum_equal(preamble, next_number):
                return next_number

            self.__replace_and_remain_sorted(preamble, first_number, next_number)

    def find_contiguous_set_that_sums_to_invalid_entry(self) -> [int]:
        invalid_entry = self.find_invalid_entry()
        contiguous_list = []
        contiguous_list_sum = 0

        iterator = 0
        while iterator < len(self.__entries):
            if contiguous_list_sum < invalid_entry:
                contiguous_list.append(self.__entries[iterator])
                contiguous_list_sum += self.__entries[iterator]
                iterator += 1
            elif contiguous_list_sum > invalid_entry and len(contiguous_list) > 0:
                contiguous_list_sum -= contiguous_list[0]
                contiguous_list = contiguous_list[1:]
            else:
                return contiguous_list

    @staticmethod
    def __replace_and_remain_sorted(sorted_list: [int], to_remove: int, to_add: int):
        removed = False
        for i in range(0, len(sorted_list)):
            if removed:
                sorted_list[i - 1] = sorted_list[i]
            elif sorted_list[i] == to_remove:
                removed = True

        added = False
        for i in range(len(sorted_list) - 2, -1, -1):
            if sorted_list[i] < to_add:
                sorted_list[i + 1] = to_add
                added = True
                break
            else:
                sorted_list[i + 1] = sorted_list[i]
        if not added:
            sorted_list[0] = to_add

    @staticmethod
    def exist_numbers_with_sum_equal(sorted_numbers: [int], expected_sum: int) -> bool:
        sorted_numbers = sorted_numbers
        left = 0
        right = len(sorted_numbers) - 1
        while (left < right):
            current_sum = sorted_numbers[left] + sorted_numbers[right]
            if current_sum < expected_sum:
                left += 1
            elif current_sum > expected_sum:
                right -= 1
            else:
                return True
        return False
