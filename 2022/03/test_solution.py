import unittest
import solution


class TestConvertAsciiToPriority(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(1, solution.convert_ascii_to_priority('a'))

    def test_uppercase(self):
        self.assertEqual(27, solution.convert_ascii_to_priority('A'))


class TestGetCommonItemPriority(unittest.TestCase):

    def test_with_rucksack(self):
        rucksack = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        self.assertEqual(16, solution.get_common_item_priority(rucksack))


class TestGetGroupBadgePriority(unittest.TestCase):

    def test_with_group(self):
        group = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']
        self.assertEqual(18, solution.get_group_badge_priority(group))


class TestSolve(unittest.TestCase):
    
    def test_with_file(self):
        self.assertEqual((157, 70), solution.solve('test.txt'))