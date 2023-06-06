import pathlib

def windows_to_posix_path(path):
    """Wrapper to convert windows path to posix"""
    return str(pathlib.PureWindowsPath(path).as_posix())
