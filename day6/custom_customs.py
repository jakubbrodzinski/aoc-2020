class CustomCustoms:
    @staticmethod
    def count_all_valid_answers(entries: [str]) -> int:
        return CustomCustoms._count(entries, CustomCustoms._count_all_valid_answers_within_group)

    @staticmethod
    def count_always_valid_answers(entries: [str]) -> int:
        return CustomCustoms._count(entries, CustomCustoms._count_always_valid_answers_within_group)

    @staticmethod
    def _count(entries: [str], count_method) -> int:
        start_line = 0
        counter = 0

        for i in range(1, len(entries)):
            if entries[i] == '':
                counter += count_method(entries[start_line:i])
                start_line = i + 1
        counter += count_method(entries[start_line:])

        return counter

    @staticmethod
    def _count_all_valid_answers_within_group(entries: [str]) -> int:
        group_answers = set()
        for entry in entries:
            for answer in entry:
                group_answers.add(answer)

        return len(group_answers)

    @staticmethod
    def _count_always_valid_answers_within_group(entries: [str]) -> int:
        first_group_answers = set()
        for answer in entries[0]:
            first_group_answers.add(answer)
        first_group_answers = list(first_group_answers)

        for entry in entries[1:]:
            if len(first_group_answers) != 0:
                first_group_answers = [answer for answer in first_group_answers if answer in entry]

        return len(first_group_answers)
