import time
import unittest
from command.sleep.sleep import Sleep


class TestSleepUsage(unittest.TestCase):
    def setUp(self) -> None:
        self.command = Sleep()

    def test_sleep_without_argument(self):
        time_before_test = time.time()

        self.command.run_command()
        time_after_test = time.time()

        self.assertEqual(0.0, round(time_after_test - time_before_test, 1))

    def test_sleep_in_second(self):
        time_before_test = time.time()

        self.command.run_command('1s')
        time_after_test = time.time()

        self.assertEqual(1.0, round(time_after_test - time_before_test, 1))

    def test_sleep_in_second_fraction(self):
        time_before_test = time.time()

        self.command.run_command('.5s')
        time_after_test = time.time()

        self.assertEqual(0.5, round(time_after_test - time_before_test, 1))

    def test_sleep_in_second_fraction_two_digits(self):
        time_before_test = time.time()

        self.command.run_command('0.58s')
        time_after_test = time.time()

        # sometimes the result can be false
        self.assertEqual(0.58, round(time_after_test - time_before_test, 2))
