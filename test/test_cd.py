import os
import pathlib
import unittest

from command.cd.cd import ChangeDirectory

class TestChangeDirectoryWithDefaultEnvironment(unittest.TestCase):
    def test_change_directory_with_no_argument(self):
        command = ChangeDirectory('default')
        
        current_directory = pathlib.Path.cwd()
        # test with no argument
        command.command()
        self.assertEqual(pathlib.Path.cwd(), pathlib.Path.home())

        #set back the current working directory
        os.chdir(str(current_directory))

    def test_change_directory_with_argument(self):
        command = ChangeDirectory()
        # test with an argument
        current_directory = pathlib.Path(__file__)

        # change directory to this folder
        command.command(current_directory.parent.parent / 'util')  # Test Fail

        self.assertEqual(str(pathlib.Path.cwd()), str(current_directory.parent.parent / 'util'))

        #set back the current working directory
        os.chdir(str(current_directory.parent))
