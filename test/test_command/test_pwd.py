import unittest
import pathlib

from command.pwd.pwd import PrintWorkingDirectory


class TestPrintWorkingDirectory(unittest.TestCase):
    def test_pwd(self):
        pwd = PrintWorkingDirectory()
        pwd_result = pwd.command()

        self.assertEqual(pwd_result, pathlib.Path.cwd())
