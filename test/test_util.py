import pathlib
import unittest

from util.conversion import windows_to_posix_path

class PathConversionTestCase(unittest.TestCase):
    def test_convert_windows_to_posix_path(self):
        _TEST_DIR = str(pathlib.Path('.').absolute())
        self.assertEqual(
            windows_to_posix_path(_TEST_DIR), str(pathlib.Path('.').absolute().as_posix()))