from day13.shuttle_search import ShuttleSearch
from utils.file_utils import read_file_lines


def run_part_one():
    input = read_file_lines('input/input-data')
    ss = ShuttleSearch(input[0], input[1])
    earliest_connection = ss.get_earliest_connection()
    return ss.calculate_output(earliest_connection[0], earliest_connection[1])


def run_part_two():
    input = read_file_lines('input/test-data')
    ss = ShuttleSearch(input[0], input[1])
    earliest_connection = ss.get_earliest_connection()
    return ss.calculate_output(earliest_connection[0], earliest_connection[1])


print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")
