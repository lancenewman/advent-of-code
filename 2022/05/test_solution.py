import unittest
from unittest import result
import solution


TEST_CRATE_STRING = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """

TEST_MOVES_STRING = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class TestSolve(unittest.TestCase):

    def test_with_file(self):
        self.assertEqual(('CMZ', 'MCD'), solution.solve('test.txt'))


class TestParseCrates(unittest.TestCase):

    def test_from_string(self):
        expected_stacks = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]

        result_stacks = solution.parse_crate_stacks(TEST_CRATE_STRING)

        # Make sure they're the same length
        self.assertEqual(len(expected_stacks), len(result_stacks))

        # Make sure the contents of each stack are the same
        for expected, result in zip(expected_stacks, result_stacks):
            self.assertListEqual(expected, result)


class TestParseMoves(unittest.TestCase):

    def test_from_string(self):
        expected_moves = [
            { 'amount': 1, 'from': 1, 'to': 0 },
            { 'amount': 3, 'from': 0, 'to': 2 },
            { 'amount': 2, 'from': 1, 'to': 0 },
            { 'amount': 1, 'from': 0, 'to': 1 },
        ]

        result_moves = solution.parse_moves(TEST_MOVES_STRING)
        self.assertEqual(len(expected_moves), len(result_moves))

        for expected, result in zip(expected_moves, result_moves):
            self.assertDictEqual(expected, result)


class TestMoveCrates(unittest.TestCase):

    def test_crane_version_9000(self):
        starting_stacks = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]

        expected_stacks = [
            ['C'],
            ['M'],
            ['P', 'D', 'N', 'Z']
        ]

        moves = [
            { 'amount': 1, 'from': 1, 'to': 0 },
            { 'amount': 3, 'from': 0, 'to': 2 },
            { 'amount': 2, 'from': 1, 'to': 0 },
            { 'amount': 1, 'from': 0, 'to': 1 },
        ]

        result_stacks = solution.move_crates(starting_stacks, moves)
        self.assertEqual(len(expected_stacks), len(result_stacks))

        for expected, result in zip(expected_stacks, result_stacks):
            self.assertListEqual(expected, result)
    
    def test_crane_version_9001(self):
        starting_stacks = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]

        expected_stacks = [
            ['M'],
            ['C'],
            ['P', 'Z', 'N', 'D']
        ]

        moves = [
            { 'amount': 1, 'from': 1, 'to': 0 },
            { 'amount': 3, 'from': 0, 'to': 2 },
            { 'amount': 2, 'from': 1, 'to': 0 },
            { 'amount': 1, 'from': 0, 'to': 1 },
        ]

        result_stacks = solution.move_crates(starting_stacks, moves, crane_version='9001')
        self.assertEqual(len(expected_stacks), len(result_stacks))

        for expected, result in zip(expected_stacks, result_stacks):
            self.assertListEqual(expected, result)


class TestGetTopCratesString(unittest.TestCase):

    def test_from_stacks(self):
        stacks = [
            ['C'],
            ['M'],
            ['P', 'D', 'N', 'Z']
        ]

        self.assertEqual('CMZ', solution.get_top_crates_string(stacks))
