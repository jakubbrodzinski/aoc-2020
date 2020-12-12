def read_file_lines(file_path: str) -> [str] :
    f = open(file_path)
    lines = f.read().split('\n')
    f.close()

    return lines

def read_file_lines_as_ints(file_path: str) -> [int] :
    f = open(file_path)
    lines = f.read().split('\n')
    f.close()

    for i in range(0,len(lines)):
        lines[i] = int(lines[i])

    return lines