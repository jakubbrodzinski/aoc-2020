from day14.docking_data import DockingData
from utils.file_utils import read_file_lines


def run_part_one():
    input = read_file_lines('input/input-data')
    return DockingData.create_version_1(input).sum_memory()


def run_part_two():
    input = read_file_lines('input/input-data')
    return DockingData.create_version_2(input).sum_memory()


print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")
