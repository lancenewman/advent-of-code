import unittest
import solution


TEST_INPUT_LINES = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]


TEST_GRID = [
    [3, 0, 3, 7, 3,],
    [2, 5, 5, 1, 2,],
    [6, 5, 3, 3, 2,],
    [3, 3, 5, 4, 9,],
    [3, 5, 3, 9, 0,],
]

class TestSolve(unittest.TestCase):

    def test_from_file(self):
        self.assertEqual((21, 8), solution.solve('test.txt'))


class TestConstructGrid(unittest.TestCase):

    def test_from_input(self):
        self.assertListEqual(TEST_GRID, solution.construct_grid(TEST_INPUT_LINES))


class TestCountVisibleTrees(unittest.TestCase):

    def test_from_grid(self):
        self.assertEqual(21, solution.count_visible_trees(TEST_GRID))


class TestIsVisible(unittest.TestCase):

    def test_exterior_column_visible(self):
        self.assertTrue(solution.is_visible((2, 0), TEST_GRID))

    def test_exterior_row_visible(self):
        self.assertTrue(solution.is_visible((0, 3), TEST_GRID))

    def test_interior_visible(self):
        self.assertTrue(solution.is_visible((1, 1), TEST_GRID))

    def test_not_visible(self):
        self.assertFalse(solution.is_visible((1, 3), TEST_GRID))


class TestIsVisibleInSubset(unittest.TestCase):

    def test_visible(self):
        self.assertTrue(solution.is_visible_in_subset(5, [4, 3]))

    def test_not_visible(self):
        self.assertFalse(solution.is_visible_in_subset(3, [4, 6, 7]))

    def test_not_visible_with_equal(self):
        self.assertFalse(solution.is_visible_in_subset(4, [4, 3, 2]))


class TestCalculateScenicScores(unittest.TestCase):

    def test_expected(self):
        expected_scores = [
            [0, 0, 0, 0, 0],
            [0, 1, 4, 1, 0],
            [0, 6, 1, 2, 0],
            [0, 1, 8, 3, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertListEqual(expected_scores, solution.calculate_scenic_scores(TEST_GRID))


class TestCalculateScenicScore(unittest.TestCase):
    
    def test_exterior(self):
        self.assertEqual(0, solution.calculate_scenic_score(3, []))

    def test_interior_one(self):
        self.assertEqual(1, solution.calculate_scenic_score(5, [3]))

    def test_interior_multiple(self):
        self.assertEqual(2, solution.calculate_scenic_score(5, [3, 5, 3]))