from command.echo.echo import Echo
import unittest


class TestEcho(unittest.TestCase):
    def setUp(self) -> None:
        self.echo_command = Echo()

    def test_echo_without_argument(self):
        result = self.echo_command.run_command()
        self.assertEqual('\n', result[0])

    def test_echo_with_one_user_argument(self):
        result = self.echo_command.run_command('hello')
        self.assertEqual(('hello', None), result)
