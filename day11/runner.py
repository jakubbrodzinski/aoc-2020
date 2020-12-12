from day11.seating_system import SeatingSystem
from day11.seating_system2 import SeatingSystem2
from utils.file_utils import read_file_lines


def run_part_one():
    ss = SeatingSystem(read_file_lines('input/input-data'))
    return ss.get_occupied_seats_count_after_stabilization()

def run_part_two():
    ss = SeatingSystem2(read_file_lines('input/input-data'))
    return ss.get_occupied_seats_count_after_stabilization()

print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")