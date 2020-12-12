from day9.encoding_error import EncodingError
from utils.file_utils import read_file_lines_as_ints


def run_part_one():
    ee = EncodingError(read_file_lines_as_ints('input/input-data'),25)
    return ee.find_invalid_entry()

def run_part_two():
    ee = EncodingError(read_file_lines_as_ints('input/input-data'), 25)
    sorted_c_set =  sorted(ee.find_contiguous_set_that_sums_to_invalid_entry())
    return sorted_c_set[0] + sorted_c_set[-1]

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")