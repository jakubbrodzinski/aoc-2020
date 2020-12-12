from day4.passport_processing import PassportProcessing
from utils.file_utils import read_file_lines


def run_part_one():
    pw = PassportProcessing(read_file_lines('input/input-data'))
    return pw.count_valid_entries()

def run_part_two():
    pw = PassportProcessing(read_file_lines('input/input-data'))
    return pw.count_fully_valid_entries()

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")