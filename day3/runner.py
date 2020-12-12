from day3.toboggan_trajectory import TobogganMap, TobogganTrajectory
from utils.file_utils import read_file_lines


def run_part_one():
    map = TobogganMap(read_file_lines('input/input-data'))
    return TobogganTrajectory(map).count_collisions()

def run_part_two():
    map = TobogganMap(read_file_lines('input/input-data'))
    trajectory = TobogganTrajectory(map);
    steps = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    mul = 1
    for elt in steps:
        mul *= trajectory.count_collisions(elt[0],elt[1])
    return mul

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")