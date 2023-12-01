import unittest
import solution


# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2


class TestSolve(unittest.TestCase):
    
    def test_from_file(self):
        self.assertTupleEqual((13, None), solution.solve('test.txt'))


class TestParseMovements(unittest.TestCase):

    def test_from_file(self):
        expected = {
            solution.RIGHT: 4,
            solution.UP: 4,
            solution.LEFT: 3,
            solution.DOWN: 1,
            solution.RIGHT: 4,
            solution.DOWN: 1,
            solution.LEFT: 5,
            solution.RIGHT: 2,
        }

        self.assertDictEqual(expected, solution.parse_movements('test.txt'))