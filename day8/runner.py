from day8.handheld_halting import HandheldHalting
from utils.file_utils import read_file_lines


def run_part_one():
    hh = HandheldHalting(read_file_lines('input/input-data'))
    return hh.get_acc_value_before_looped()

def run_part_two():
    hh = HandheldHalting(read_file_lines('input/input-data'))
    return hh.get_acc_value_with_changed_single_command()

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")