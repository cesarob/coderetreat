class Generation:
    pass


class Cell:
    def __init__(self):
        self.is_alive = True

    @property
    def neighbours(self):
        return [Cell()]

    def die(self):
        self.is_alive = False


def next_generation(generation):
    return generation
