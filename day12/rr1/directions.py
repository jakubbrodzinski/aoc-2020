class North:
    @staticmethod
    def move(position: (int, int), distance: int) -> (int, int):
        return position[0], position[1] - distance

    @staticmethod
    def move_left(degree: int):
        return [North, East, South, West][-((degree // 90) % 4)]

    @staticmethod
    def move_right(degree: int):
        return [North, East, South, West][(degree // 90) % 4]

    @staticmethod
    def move_forward(position: (int, int), distance: int):
        return North.move(position, distance)


class East:
    @staticmethod
    def move(position: (int, int), distance: int) -> (int, int):
        return position[0] + distance, position[1]

    @staticmethod
    def move_left(degree: int):
        return [East, South, West, North][-((degree // 90) % 4)]

    @staticmethod
    def move_right(degree: int):
        return [East, South, West, North][(degree // 90) % 4]

    @staticmethod
    def move_forward(position: (int, int), distance: int):
        return East.move(position, distance)


class South:
    @staticmethod
    def move(position: (int, int), distance: int) -> (int, int):
        return position[0], position[1] + distance

    @staticmethod
    def move_left(degree: int):
        return [South, West, North, East][-((degree // 90) % 4)]

    @staticmethod
    def move_right(degree: int):
        return [South, West, North, East][(degree // 90) % 4]

    @staticmethod
    def move_forward(position: (int, int), distance: int):
        return South.move(position, distance)


class West:
    @staticmethod
    def move(position: (int, int), distance: int) -> (int, int):
        return position[0] - distance, position[1]

    @staticmethod
    def move_left(degree: int):
        return [West, North, East, South][-((degree // 90) % 4)]

    @staticmethod
    def move_right(degree: int):
        return [West, North, East, South][(degree // 90) % 4]

    @staticmethod
    def move_forward(position: (int, int), distance: int):
        return West.move(position, distance)
