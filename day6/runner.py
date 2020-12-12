from day6.custom_customs import CustomCustoms
from utils.file_utils import read_file_lines


def run_part_one():
    return CustomCustoms.count_all_valid_answers(read_file_lines('input/input-data'))

def run_part_two():
    return CustomCustoms.count_always_valid_answers(read_file_lines('input/input-data'))


print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")