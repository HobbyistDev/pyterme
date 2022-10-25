import unittest

from command.which.which import Which


class TestWhich(unittest.TestCase):
    def setUp(self) -> None:
        self.which_command = Which()

    def test_which_without_argument(self):
        command_result = self.which_command.run_command()
        self.assertEqual((None, None), command_result)

    def test_which_with_valid_argument(self):
        pass

    def test_which_with_invalid_argument(self):
        command_result = self.which_command.run_command('dfghj')
        self.assertEqual((None, None), command_result)
