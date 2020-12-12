class HandheldHalting:
    JMP = 'jmp'
    NOP = 'nop'
    ACC = 'acc'
    def __init__(self, file_input):
        self.__commands = []
        for line in file_input:
            split = line.split(' ')
            self.__commands.append((split[0], int(split[1])))

        print(self.__commands)

    def get_acc_value_before_looped(self):
        return self.__execute_commands()[1]

    def get_acc_value_with_changed_single_command(self):
        for line in range(0,len(self.__commands)):
            command = self.__commands[line]
            if command[0] == HandheldHalting.JMP:
                self.__commands[line] = HandheldHalting.NOP, command[1]
                ended, acc = self.__execute_commands()
                self.__commands[line] = HandheldHalting.JMP, command[1]
                if ended:
                    return acc
            elif command[1] == HandheldHalting.NOP:
                self.__commands[line] = HandheldHalting.JMP, command[1]
                ended, acc = self.__execute_commands()
                self.__commands[line] = HandheldHalting.NOP, command[1]
                if ended:
                    return acc

    def __execute_commands(self):
        visited_lines = [False] * len(self.__commands)
        acc = 0
        current_line = 0
        while current_line < len(self.__commands):
            command = self.__commands[current_line]
            if visited_lines[current_line]:
                return False, acc
            visited_lines[current_line] = True

            if HandheldHalting.ACC == command[0]:
                acc += command[1]
                current_line += 1
            elif HandheldHalting.JMP == command[0]:
                current_line += command[1]
            elif HandheldHalting.NOP == command[0]:
                current_line += 1

        return True, acc
