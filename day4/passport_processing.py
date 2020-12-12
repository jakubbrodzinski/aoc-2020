import re

class PassportProcessing:
    __required_sections = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    __optional_sections = ['cid']

    def __init__(self, input: [str]):
        self.__password_entries = self.__parse(input)
        self.__validator = PasswordValidator()

    def size(self):
        return len(self.__password_entries)

    def get_entry(self, i: int):
        return self.__password_entries[i]

    def __parse(self, input: [str]) -> [{str: str}]:
        output = []
        accumulator = {}
        for line in input:
            if line != '':
                for entry in line.split(' '):
                    [key, value] = entry.split(':')
                    accumulator[key] = value
            else:
                output.append(accumulator)
                accumulator = {}
        if len(accumulator) != 0:
            output.append(accumulator)
        return output

    def count_valid_entries(self):
        valid_entries_counter = 0
        for entry in self.__password_entries:
            if self.__validator.validate_entry(entry,False):
                valid_entries_counter += 1
        return valid_entries_counter

    def count_fully_valid_entries(self):
        valid_entries_counter = 0
        for entry in self.__password_entries:
            if self.__validator.validate_entry(entry,True):
                valid_entries_counter += 1
        return valid_entries_counter

    def __is_entry_valid(self, entry):
        for required_section in self.__required_sections:
            if not required_section in entry:
                return False
        return True


class PasswordValidator:
    _ecl_valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    __required_sections = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    __optional_sections = ['cid']

    def validate_entry(self, entry, extended_validation=False):
        if extended_validation:
            return self.__extended_validation(entry)
        else:
            return self.__simple_validation(entry)

    def __simple_validation(self, entry):
        for required_section in self.__required_sections:
            if not required_section in entry:
                return False
        return True

    def __extended_validation(self, entry):
        return self.__simple_validation(entry) and self.validate_byr(entry['byr']) and \
               self.validate_iyr(entry['iyr']) and self.validate_eyr(entry['eyr']) and \
               self.validate_hgt(entry['hgt']) and self.validate_hcl(entry['hcl']) and \
               self.validate_ecl(entry['ecl']) and self.validate_pid(entry['pid'])

    def validate_byr(self, value):
        return 1920 <= int(value) <= 2002

    def validate_iyr(self, value):
        return 2010 <= int(value) <= 2020

    def validate_eyr(self, value):
        return 2020 <= int(value) <= 2030

    def validate_hgt(self, value):
        if len(value) < 2:
            return False
        units = value[-2:]
        int_value = int(value[:-2])
        return (units == 'in' and 59 <= int_value <= 76) or (units == 'cm' and 150 <= int_value <= 193)

    def validate_hcl(self, value):
        return bool(re.match('#[0-9a-f]{6}', value))

    def validate_ecl(self, value):
        return value in self._ecl_valid_values

    def validate_pid(self, value):
        return len(value) == 9 and bool(re.match('0*[1-9]+', value))
