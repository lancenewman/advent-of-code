import unittest
import solution

class TestEvaluateRoundPart1(unittest.TestCase):
    
    def test_win(self):
        elf_move = "A"
        my_move = "Y"
        self.assertEqual(8, solution.evaluate_round_part_1(elf_move, my_move))

    def test_loss(self):
        elf_move = "B"
        my_move = "X"
        self.assertEqual(1, solution.evaluate_round_part_1(elf_move, my_move))

    def test_draw(self):
        elf_move = "C"
        my_move = "Z"
        self.assertEqual(6, solution.evaluate_round_part_1(elf_move, my_move))


class TestEvaluateRoundPart2(unittest.TestCase):

    def test_win(self):
        elf_move = "C"
        outcome = "Z"
        self.assertEqual(7, solution.evaluate_round_part_2(elf_move, outcome))

    def test_draw(self):
        elf_move = "A"
        outcome = "Y"
        self.assertEqual(4, solution.evaluate_round_part_2(elf_move, outcome))

    def test_lose(self):
        elf_move = "B"
        outcome = "X"
        self.assertEqual(1, solution.evaluate_round_part_2(elf_move, outcome))


class TestSolve(unittest.TestCase):

    def test_with_file(self):
        file = "test.txt"
        self.assertEqual((15, 12), solution.solve(file))