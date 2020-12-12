from day5.BinaryBoarding import BinaryBoardingParser
from utils.file_utils import read_file_lines


def run_part_one():
    max_seat_id = 0
    for line in read_file_lines('input/input-data'):
        seat_id = BinaryBoardingParser.parse(line)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def run_part_two():
    seat_ids = []
    for line in read_file_lines('input/input-data'):
        seat_ids.append(BinaryBoardingParser.parse(line))
    seat_ids.sort()
    for i in range(1, len(seat_ids)):
        if seat_ids[i - 1] != seat_ids[i] - 1:
            return seat_ids[i] - 1


print(f"Part one: {run_part_one()}")
print(f"Part two: {run_part_two()}")
