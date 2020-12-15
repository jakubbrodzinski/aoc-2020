class ShuttleSearch:
    def __init__(self, timestamp: str, lines_entry: str):
        self.__timestamp = int(timestamp)
        self.__lines = []
        self.__lines_with_constraints = []
        lines = lines_entry.split(',')
        for i in range(0, len(lines)):
            if lines[i] != 'x':
                line_int = int(lines[i])
                self.__lines.append(line_int)
                self.__lines_with_constraints.append((line_int, line_int - i))

        self.__lines_with_constraints.sort(reverse=True, key=lambda x: x[0])

    def get_earliest_connection(self):
        min_wait_time = self.__lines[0] - (self.__timestamp % self.__lines[0])
        line = self.__lines[0]
        for i in range(1, len(self.__lines)):
            wait_time = self.__lines[i] - (self.__timestamp % self.__lines[i])
            if wait_time < min_wait_time:
                min_wait_time = wait_time
                line = self.__lines[i]

        return line, min_wait_time + self.__timestamp

    def calculate_output(self, line: int, timestamp: int):
        wait_time = timestamp - self.__timestamp
        return line * wait_time

    def get_timestamp_with_constraints(self):
        mod = self.__lines_with_constraints[0][0]
        start_value = self.__lines_with_constraints[0][1]
        for i in range(1, len(self.__lines_with_constraints)):
            next_mod = self.__lines_with_constraints[i][0]
            expected_remainder = self.__lines_with_constraints[i][1]
            start_value = self.__chinese_remainder_theorem(start_value, mod, expected_remainder, next_mod)
            mod *= next_mod
        return start_value

    @staticmethod
    def __chinese_remainder_theorem(start_value, mod, expected_remainder, mod_next) -> int:
        while start_value % mod_next != expected_remainder:
            start_value += mod
        return start_value
