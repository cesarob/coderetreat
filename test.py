from expects import *
from doublex import *
from doublex_expects import *
from expects.matchers import Matcher


from game import *

with description('The Game Of Life'):

    with context("Game Creation"):
        with before.each:
            self.game = Game(3, 2)

        with it('is created with a dimension'):
            expect(self.game.width).to(equal(3))
            expect(self.game.height).to(equal(2))

        with it("has a board"):
            expect(self.game.board).to(be_a(Board))

    with context("Game"):
        with before.each:
            self.game = Game(3, 3)

        with it("changes board in every iteration"):
            current_board = self.game.board
            board = self.game.next_generation()
            expect(board).not_to(equal(current_board))

        with it("cannot change board if game is finished"):
            self.game.is_finished = True
            expect(self.game.next_generation).to(raise_error)

        with it("finishes when global cell status is maintained"):
            not_evolving_status = [[0, 0, 0], [1, 1, 0], [0, 1, 1]]
            set_init_status(self.game, not_evolving_status)
            self.game.next_generation()
            expect(self.game.is_finished).to(equal(True))
            expect(get_game_status(self.game)).to(equal(not_evolving_status))

    with context("Board"):
        with before.each:
            self.game = Game(3, 3)

        with it("must have cells"):
            cell = self.game.board.get_cell(0, 0)
            expect(cell).to(be_a(Cell))


def set_init_status(game, status):
    game.status = status


def get_game_status(game):
    return game.status
