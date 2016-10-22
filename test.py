from expects import *
from doublex import *
from doublex_expects import *

from game import *

with description('The Game Of Life'):
    with context('Cell next state'):
        with it('under_population (<2)'):
            expect(next_state(1, 1)).to(equal(0))
            expect(next_state(1, 2)).to(equal(1))

        with it('survival (=2,3)'):
            expect(next_state(1, 2)).to(equal(1))
            expect(next_state(1, 3)).to(equal(1))
            expect(next_state(0, 2)).to(equal(0))

        with it('overcrowding (>3)'):
            expect(next_state(1, 4)).to(equal(0))
