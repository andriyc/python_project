import os
import sys
from configparser import ConfigParser


class ProjectSettings:
    project_properties: ConfigParser

    def __init__(self, file: str):
        print('init: ' + sys.path[0])
        self.project_properties = ConfigParser()
        self.project_properties.read(file)

    def get(self, section: str, item: str):
        return self.project_properties.get(section, item)

    def is_true(self, section: str, item: str) -> bool:
        return self.project_properties.get(section, item).lower().strip() == 'true'


config_folder_abspath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
project_properties = ProjectSettings(config_folder_abspath + '/config.ini')

