import pathlib
import json


def shell_set_configuration(conf_path='default'):
    if conf_path == 'default':
        with open(pathlib.Path("conf/shell_conf.json")) as file:
            json_conf_file = json.load(file)
        return json_conf_file.get('shell') or {}
