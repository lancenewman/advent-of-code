import unittest
import solution


class TestSolve(unittest.TestCase):
    
    def test_with_file(self):
        self.assertEqual((7, 19), solution.solve('test.txt'))


class TestIsUnique(unittest.TestCase):

    def test_unique(self):
        self.assertTrue(solution.is_unique('abcd'))

    def test_not_unique(self):
        self.assertFalse(solution.is_unique('abac'))


class TestFindStartOfUniqueSequenceInSignal(unittest.TestCase):

    def test_from_string(self):
        signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        self.assertEqual(19, solution.find_start_of_unique_sequence_in_signal(signal, 14))


class TestFindStartOfMessage(unittest.TestCase):

    def test_from_string(self):
        test_signals = {
            'mjqjpqmgbljsphdztnvjfqwrcgsmlb': 19,
            'bvwbjplbgvbhsrlpgdmjqwftvncz': 23,
            'nppdvjthqldpwncqszvftbrmjlhg': 23,
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': 29,
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': 26,
        }

        for signal, expected_start_of_packet in test_signals.items():
            self.assertEqual(expected_start_of_packet, solution.find_start_of_message(signal))


class TestFindStartOfPacket(unittest.TestCase):
    
    def test_from_string(self):
        test_signals = {
            'mjqjpqmgbljsphdztnvjfqwrcgsmlb': 7,
            'bvwbjplbgvbhsrlpgdmjqwftvncz': 5,
            'nppdvjthqldpwncqszvftbrmjlhg': 6,
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': 10,
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': 11,
        }

        for signal, expected_start_of_packet in test_signals.items():
            self.assertEqual(expected_start_of_packet, solution.find_start_of_packet(signal))