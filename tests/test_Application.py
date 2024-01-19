import logging
import unittest
import json
import pygame
import os

from json import JSONDecodeError
from src.Application import Application

class TestApplication(unittest.TestCase):
    """
    Tests the Application class.
    """
    configuration_path = "tests/res/configuration_files"
    created_files = None
    

    def setUp(self) -> None:
        return super().setUp()
    
    
    def tearDown(self) -> None:
        if not self.created_files is None:
            for file in self.created_files:
                os.remove(file)

            self.created_files = None        

        return super().tearDown()


    def test_no_configuration_file(self):
        """
        Tests the Application class with no configuration file.
        """
        application = Application()

        # Test log level
        self.assertEqual(application.log_level_name, "error")

        # Test resolution
        self.assertEqual(application.width, application.DEFAULT_WIDTH)
        self.assertEqual(application.height, application.DEFAULT_HEIGHT)



    def test_nonexistant_configuration_file(self):
        """
        Tests the Application class with a nonexistant configuration file.
        """
        with self.assertRaises(FileNotFoundError):
            application = Application(configuration_file="invalid_file.json")


    def test_invalid_json_file(self):
        """
        Tests the Application class with an invalid JSON file.
        """
        self.created_files = [
            f"""{self.configuration_path}/invalid_file.json"""
        ]

        with open(f"""{self.configuration_path}/invalid_file.json""", "w") as file:
            file.write("This is not JSON")

        with self.assertRaises(JSONDecodeError):
            application = Application(configuration_file=f"""{self.configuration_path}/invalid_file.json""")


    def test_configuration_file_with_invalid_options(self):
        """
        Tests the Application class with an configuration file that has invalid options.
        """
        self.created_files = [
            f"""{self.configuration_path}/invalid_configuration.json"""
        ]

        invalid_configuration = {
            "log_level": "invalid",
            "resolution": "invalid",
        }

        with open(f"{self.configuration_path}/invalid_configuration.json", "w") as file:
            json.dump(invalid_configuration, file)
        
        with self.assertRaises(ValueError):
            application = Application(configuration_file="tests/res/configuration_files/invalid_configuration.json")


    def test_configuration_file_with_valid_options(self):
        """
        Tests the Application class with an configuration file that has valid options.

        """
        self.created_files = [ 
            f"""{self.configuration_path}/valid_configuration.json"""
        ]

        valid_configuration = {
            "log_level": "info",
            "resolution": (1920, 1080),
        }

        with open(f"""{self.configuration_path}/valid_configuration.json""", "w") as file:
            json.dump(valid_configuration, file)
        
        application = Application(configuration_file=f"""{self.configuration_path}/valid_configuration.json""")

        # Test log level
        self.assertEqual(application.log_level_name, "info")
        self.assertEqual(application.log_level, logging.INFO)

        # Test resolution
        self.assertEqual(application.width, 1920)
        self.assertEqual(application.height, 1080)



    def test_configuration_file_with_partial_options(self):
        """
        Tests the Application class with an configuration file that has partial options.
        """
        self.created_files = [
            f"""{self.configuration_path}/partial_configuration.json"""
        ]

        partial_configuration = {
            "log_level": "info",
        }

        with open(f"""{self.configuration_path}/partial_configuration.json""", "w") as file:
            json.dump(partial_configuration, file)
        
        application = Application(configuration_file=f"""{self.configuration_path}/partial_configuration.json""")

        # Test log level
        self.assertEqual(application.log_level_name, "info")
        self.assertEqual(application.log_level, logging.INFO)

        # Test resolution
        self.assertEqual(application.width, application.DEFAULT_WIDTH)
        self.assertEqual(application.height, application.DEFAULT_HEIGHT)


    def test_setup_pygame(self):
        """
        Tests the setup_pygame method.
        """
        application = Application()

        expected_width = application.DEFAULT_WIDTH
        expected_height = application.DEFAULT_HEIGHT
        excepted_caption = (f"pygame window", "pygame window")

        self.assertEqual(pygame.display.get_caption(), excepted_caption)
        self.assertEqual(pygame.display.get_window_size(), (expected_width, expected_height))


    def test_stop(self):
        """
        Tests the stop method.
        """
        application = Application()
        application.start()
        application.stop()

        self.assertFalse(application.running)


    def test_game_responds_to_quit_event(self):
        """
        Tests that the game responds to the quit event.
        """
        application = Application()
        application.start()

        pygame.event.post(pygame.event.Event(pygame.QUIT))

        self.assertFalse(application.running)

        

if __name__ == "__main__":
    unittest.main()
    