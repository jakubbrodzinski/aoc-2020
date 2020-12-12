from day7.handy_haversacks import HandyHaversacks, HandyHaversacks2
from utils.file_utils import read_file_lines

SHINY_BAG = 'shiny gold'
def run_part_one():
    hh = HandyHaversacks(read_file_lines('input/input-data'))
    return hh.count_valid_outermost_bags(SHINY_BAG)


def run_part_two():
    hh2 = HandyHaversacks2(read_file_lines('input/input-data'))
    return hh2.count_inner_bags(SHINY_BAG)


print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")

