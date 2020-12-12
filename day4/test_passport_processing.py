from unittest import TestCase

from day4.passport_processing import PassportProcessing, PasswordValidator
from utils.file_utils import read_file_lines


class TestPassportProcessing(TestCase):
    def test_parse(self):
        pw = PassportProcessing(["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm"])
        self.assertEqual(pw.size(), 1)

        expected_entry = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                          'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
        self.assertEqual(pw.get_entry(0), expected_entry)

    def test_parse_test_data(self):
        test_input = read_file_lines('input/test-data')
        self.assertEqual(PassportProcessing(test_input).size(), 4)

    def test_count_valid_entries(self):
        test_input = read_file_lines('input/test-data')
        pw = PassportProcessing(test_input)
        self.assertEqual(pw.count_valid_entries(), 2)


class TestFieldValidator(TestCase):
    def test_validate_invalid_entries(self):
        validator = PasswordValidator()
        self.assertFalse(validator.validate_entry(
            {'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb', 'hgt': '170', 'pid': '186cm', 'iyr': '2018',
             'byr': '1926'}))
        self.assertFalse(validator.validate_entry(
            {'iyr': '2019', 'hcl': '#602927', 'eyr': '1967', 'hgt': '170cm', 'ecl': 'grn', 'pid': '012533040',
             'byr': '1946'}))
        self.assertFalse(validator.validate_entry(
            {'hcl': 'dab227', 'iyr': '2012', 'ecl': 'brn', 'hgt': '182cm', 'pid': '021572410', 'eyr': '2020',
             'byr': '1992',
             'cid': '277'}))
        self.assertFalse(validator.validate_entry(
            {'hgt': '59cm', 'ecl': 'zzz', 'eyr': '2038', 'hcl': '74454a', 'iyr': '2023', 'pid': '3556412378',
             'byr': '2007'}))

    def test_validate_valid_entries(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_entry(
            {'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012', 'eyr': '2030', 'byr': '1980',
             'hcl': '#623a2f'}))
        self.assertTrue(validator.validate_entry(
            {'eyr': '2029', 'ecl': 'blu', 'cid': '129', 'byr': '1989', 'iyr': '2014', 'pid': '896056539',
             'hcl': '#a97842',
             'hgt': '165cm'}))
        self.assertTrue(validator.validate_entry(
            {'hcl': '#888785', 'hgt': '164cm', 'byr': '2001', 'iyr': '2015', 'cid': '88', 'pid': '545766238',
             'ecl': 'hzl',
             'eyr': '2022'}))
        self.assertTrue(validator.validate_entry(
            {'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu', 'byr': '1944', 'eyr': '2021',
             'pid': '093154719'}))

    def test_validate_byr(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_byr('2002'))
        self.assertFalse(validator.validate_byr('2003'))

    def test_validate_iyr(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_ecl('brn'))
        self.assertFalse(validator.validate_ecl('wat'))

    def test_validate_eyr(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_ecl('brn'))
        self.assertFalse(validator.validate_ecl('wat'))

    def test_validate_hgt(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_hgt('60in'))
        self.assertTrue(validator.validate_hgt('190cm'))
        self.assertFalse(validator.validate_hgt('190in'))
        self.assertFalse(validator.validate_hgt('190'))

    def test_validate_hcl(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_hcl('#123abc'))
        self.assertFalse(validator.validate_hcl('#123abz'))
        self.assertFalse(validator.validate_hcl('123abc'))

    def test_validate_ecl(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_ecl('brn'))
        self.assertFalse(validator.validate_ecl('wat'))

    def test_validate_pid(self):
        validator = PasswordValidator()
        self.assertTrue(validator.validate_pid('000000001'))
        self.assertFalse(validator.validate_pid('0123456789'))
