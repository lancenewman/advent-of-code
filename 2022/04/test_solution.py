import unittest
import solution


class TestExtractIntegerBounds(unittest.TestCase):

    def test_get_bounds(self):
        self.assertListEqual([1, 2], solution.extract_integer_bounds('1-2'))


class TestAssignmentFullyCovered(unittest.TestCase):

    def test_covered(self):
        a1 = '2-8'
        a2 = '3-7'
        self.assertTrue(solution.assignment_fully_covered(a1, a2))

    def test_partially_covered(self):
        a1 = '5-7'
        a2 = '7-9'
        self.assertFalse(solution.assignment_fully_covered(a1, a2))

    def test_not_covered(self):
        a1 = '2-4'
        a2 = '6-8'
        self.assertFalse(solution.assignment_fully_covered(a1, a2))


class TestAssignmentPartiallyCovered(unittest.TestCase):

    def test_covered(self):
        a1 = '2-8'
        a2 = '3-7'
        self.assertTrue(solution.assignment_partially_covered(a1, a2))

    def test_partially_covered(self):
        a1 = '5-7'
        a2 = '7-9'
        self.assertTrue(solution.assignment_partially_covered(a1, a2))

    def test_not_covered(self):
        a1 = '2-4'
        a2 = '6-8'
        self.assertFalse(solution.assignment_partially_covered(a1, a2))


class TestContainsFullyCoveredSection(unittest.TestCase):

    def test_fully_contained(self):
        assignments = '2-8,3-7'
        self.assertTrue(solution.contains_fully_covered_section(assignments))

    def test_partially_contained(self):
        assignments = '5-7,7-9'
        self.assertFalse(solution.contains_fully_covered_section(assignments))

    def test_not_contained(self):
        assignments = '2-4,6-8'
        self.assertFalse(solution.contains_fully_covered_section(assignments))


class TestContainsPartiallyCoveredSection(unittest.TestCase):

    def test_fully_contained(self):
        assignments = '2-8,3-7'
        self.assertTrue(solution.contains_partially_covered_section(assignments))

    def test_partially_contained(self):
        assignments = '5-7,7-9'
        self.assertTrue(solution.contains_partially_covered_section(assignments))

    def test_not_contained(self):
        assignments = '2-4,6-8'
        self.assertFalse(solution.contains_partially_covered_section(assignments))


class TestSolve(unittest.TestCase):

    def test_with_file(self):
        self.assertEqual((2, 4), solution.solve('test.txt'))