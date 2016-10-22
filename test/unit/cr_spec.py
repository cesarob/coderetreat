from expects import *
from doublex import *
from doublex_expects import *
from expects.matchers import Matcher


from game import Generation, Cell, next_generation

with description('The Game Of Life'):
    with it('moves from one generation to another'):
        a_generation = Generation()
        expect(next_generation(a_generation)).to(be_a(Generation))

    with context("Cell"):
        with it("is alive when created"):
            a_cell = Cell()
            expect(a_cell.is_alive).to(be_true)

        with it("can die"):
            a_cell = Cell()
            a_cell.die()
            expect(a_cell.is_alive).to(be_false)

        with it("has at least one neighbour"):
            a_cell = Cell()
            expect(a_cell.neighbours).to(have_length(be_above_or_equal(1)))

        with it('has cells as neighbours'):
            a_cell = Cell()

            expect(a_cell.neighbours).to(be_all_cells)

class be_all_cells(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, neighbours):
        for neighbour in a_neighbours:
            expect(neighbour).to(be_a(Cell))
        return True, ['neigbouts not cells']
