
class Cell:
    pass


class Board:
    def get_cell(self, x, y):
        return Cell()


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = Board()
        self.is_finished = False
        self.status = None

    def next_generation(self):
        if (self.is_finished):
            raise Exception()

        self.board = Board()
        self.is_finished = True
