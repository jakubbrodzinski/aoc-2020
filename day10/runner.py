from day10.adapter_array import AdapterArray
from utils.file_utils import read_file_lines_as_ints


def run_part_one():
    aa = AdapterArray(read_file_lines_as_ints('input/input-data'))
    diffs =  aa.get_diffs_tuple()
    return diffs[0]*diffs[2]

def run_part_two():
    aa = AdapterArray(read_file_lines_as_ints('input/input-data'))
    return aa.count_possible_connections()

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")