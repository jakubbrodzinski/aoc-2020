from day12.rr1.rain_risk import RainRisk
from day12.rr2.rain_risk2 import RainRisk2
from utils.file_utils import read_file_lines


def run_part_one():
    rr = RainRisk(read_file_lines('input/input-data'))
    return RainRisk.get_manhattan_distance(rr.follow_instructions())

def run_part_two():
    rr2 = RainRisk2(read_file_lines('input/input-data'))
    return RainRisk.get_manhattan_distance(rr2.follow_instructions())

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")