import re


class DockingData:
    __create_key = object()

    __mask_format = 'mask = (.*)'
    __memory_asignment_format = 'mem\[([0-9]+)\] = ([0-9]+)'

    def __init__(self, create_key, entries: [str], first_version: bool):
        assert (create_key == DockingData.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"
        self.__memory = {}
        if first_version:
            self.__first_version_computation(entries)
        else:
            self.__second_version_computation(entries)

    def __first_version_computation(self, entries: [str]):
        current_mask = None
        for entry in entries:
            findall = re.findall(self.__mask_format, entry)
            if len(findall) != 0:
                current_mask = BitmapSystem(findall[0])
            else:
                mem_assignment_findall = re.findall(self.__memory_asignment_format, entry)[0]
                self.__memory[mem_assignment_findall[0]] = current_mask.proccess(mem_assignment_findall[1])

    def __second_version_computation(self, entries: [str]):
        current_mask = None
        for entry in entries:
            findall = re.findall(self.__mask_format, entry)
            if len(findall) != 0:
                current_mask = BitmapSystem2(findall[0])
            else:
                mem_assignment_findall = re.findall(self.__memory_asignment_format, entry)[0]
                for mem_addr in current_mask.process(mem_assignment_findall[0]):
                    self.__memory[mem_addr] = int(mem_assignment_findall[1])

    @classmethod
    def create_version_1(cls, entries: [str]):
        return DockingData(cls.__create_key, entries, True)

    @classmethod
    def create_version_2(cls, entries: [str]):
        return DockingData(cls.__create_key, entries, False)

    def sum_memory(self):
        sum = 0
        for key, value in self.__memory.items():
            sum += value

        return sum


class BitmapSystem:
    def __init__(self, bitmask: str):
        self._and_mask = self.__get_and_mask(bitmask)
        self._or_mask = self.__get_or_mask(bitmask)

    def __get_or_mask(self, bitmask: str):
        or_mask = 0
        for bit in bitmask:
            or_mask = or_mask << 1
            if bit == '1':
                or_mask += 1

        return or_mask

    def __get_and_mask(self, bitmask: str):
        and_mask = 0
        for bit in bitmask:
            and_mask = and_mask << 1
            if bit != '0':
                and_mask += 1

        return and_mask

    def proccess(self, number: str):
        return (int(number) & self._and_mask) | self._or_mask


class BitmapSystem2:
    def __init__(self, bitmask: str):
        self.__masks = self.__get_masks(bitmask, 0, 0)
        self.__and_mask = self.__get_and_mask(bitmask)

    def process(self, number: str):
        return list(map(lambda mask: mask | int(number) & self.__and_mask, self.__masks))

    def __get_masks(self, bitmask: str, value, index) -> [int]:
        while index < len(bitmask):
            if bitmask[index] == 'X':
                return self.__get_masks(bitmask, value << 1, index + 1) + self.__get_masks(bitmask, (value + 1) << 1,
                                                                                           index + 1)
            elif bitmask[index] == '0':
                value = value << 1
            else:
                value = (value + 1) << 1
            index += 1
        return [value >> 1]

    def __get_and_mask(self, bitmask):
        and_mask = 0
        for bit in bitmask:
            if bit == 'X':
                and_mask = and_mask << 1
            else:
                and_mask = (and_mask + 1) << 1
        return and_mask >> 1
