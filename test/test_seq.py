import unittest

from command.seq.seq import Sequence


class TestSequence(unittest.TestCase):
    def setUp(self) -> None:
        self.command = Sequence()

    def test_sequence_with_no_argument(self):
        result = self.command.run_command()
        self.assertEqual(result, (None, None))

    def test_sequence_with_one_argument(self):
        pass

    def test_sequence_with_two_argument(self):
        pass

    def test_sequence_with_three_argument(self):
        pass
