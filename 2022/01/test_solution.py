import unittest
import solution


class TestSolve(unittest.TestCase):

    def test_file(self):
        file = 'test.txt'
        self.assertEqual(24000, max(solution.solve(file)))
        self.assertEqual(45000, sum(solution.solve(file)))