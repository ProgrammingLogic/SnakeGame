import logging
import unittest
import json
import pygame
import os

from json import JSONDecodeError
# Not sure where to use MagicMock, but it's freaking cool and I want to use it!
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
from unittest.mock import MagicMock

from src.Application import Application
import os


class TestApplication(unittest.TestCase):
    """
    Test the Application class.
    """
    def setUp(self):
        command_line_arguments = {

        }

        self.application = Application(command_line_arguments)
        self.files_to_delete = []
        self.configuration_file_dir = os.path.join(os.path.dirname(__file__), "res", "configurations")


    def tearDown(self):
        self.application = None
        
        for file in self.files_to_delete:
            os.remove(file)


    def test_load_invalid_configuration_file(self):
        """
        Test that the configuration file is not loaded if it contains invalid data.

        TODO:
            - Fix Application.load_configuration_file() so that this test passes.
        """
        # Set up a mock configuration file that contains invalid data
        mock_config_file = f"""{self.configuration_file_dir}/invalid_config.json"""

        invalid_configuration = {
            "log_level": "invalid",
            "log_level_name": "invalid",
            "log_directory": "invalid",
            "log_file": "invalid",
            "width": "invalid",
            "height": "invalid"
        }

        os.makedirs(os.path.dirname(mock_config_file), exist_ok=True)

        with open(mock_config_file, "w") as f:
            json.dump(invalid_configuration, f, indent=4)

        # Load the configuration file
        self.application.configuration_file = mock_config_file
        self.assertRaises(AttributeError, self.application.load_configuration_file)

        # TODO
        #  - Assert that the configuration file was not loaded successfully
        


    def test_load_valid_configuration_file(self):
        # Set up a mock configuration file that contains valid data
        mock_config_file = f"""{self.configuration_file_dir}/valid_config.json"""

        full_configuration = {
            "log_level": "info",
            "log_level_name": "info",
            "log_directory": "logs",
            "log_file": "game.log",
            "width": 1920,
            "height": 1080
        }

        os.makedirs(os.path.dirname(mock_config_file), exist_ok=True)

        with open(mock_config_file, "w") as f:
            json.dump(full_configuration, f, indent=4)


        # Load the configuration file
        self.application.configuration_file = mock_config_file
        self.application.load_configuration_file()

        # Assert that the configuration file was loaded successfully
        self.assertEqual(self.application.width, 1920)
        self.assertEqual(self.application.height, 1080)


    def test_load_partial_configuration_file(self):
        # Set up a mock configuration file that contains partial data
        mock_config_file = f"""{self.configuration_file_dir}/partial_config.json"""

        partial_configuration = {
            "log_level": "info",
        }

        # file_contents = json.dumps(partial_configuration)

        os.makedirs(os.path.dirname(mock_config_file), exist_ok=True)

        with open(mock_config_file, "w") as f:
            json.dump(partial_configuration, f, indent=4)

        # Load the configuration file
        self.application.configuration_file = mock_config_file
        self.application.load_configuration_file()

        # Assert that the configuration file was loaded successfully
        self.assertEqual(self.application.log_level, logging.INFO)
        self.assertEqual(self.application.log_level_name, "info")


        if __name__ == "__main__":
            unittest.main()


if __name__ == "__main__":
    unittest.main()

    