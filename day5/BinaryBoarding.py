class BinaryBoardingParser:
    @staticmethod
    def parse(boarding_pass: str) -> int:
        row_id = BinaryBoardingParser.__binary_search(boarding_pass[0:7], 'F', 'B', 127)
        column_id = BinaryBoardingParser.__binary_search(boarding_pass[-3:], 'L', 'R', 7)
        return row_id * 8 + column_id

    @staticmethod
    def __binary_search(string, lower_char, upper_char, max_value) -> int:
        left = 0
        right = max_value
        for char in string:
            if char == lower_char:
                right = (left + right) // 2
            elif char == upper_char:
                left = (right + left) // 2 + 1

        return left;
