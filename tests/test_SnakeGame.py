import logging
import unittest
from src.Application import Application


class TestApplication(unittest.TestCase):
    def test_process_configuration_file(self):
        # Ensure the process configuration file method can handle a valid configuration file
        kwargs = {"configuration_file": "Tests/res/test_configuration.json"}
        game = Application(**kwargs)
        self.assertTrue(game.log_level == logging.DEBUG)

        # Ensure the process configuration file method can handle an invalid configuration file
        kwargs = {"configuration_file": "Tests/res/invalid_configuration.json"}
        self.assertRaises(FileNotFoundError, Application, **kwargs)
        

    def test_process_configuration(self):
        # Ensure that the debug argument is set to False by default
        game = Application()
        game.process_configuration()
        self.assertTrue(game.log_level == logging.ERROR)

        # Ensure the process arguments method can handle the log level argument
        kwargs = {"log_level": "debug"}
        game.process_configuration(**kwargs)
        self.assertTrue(game.log_level == logging.DEBUG)

        kwargs = {"log_level": "info"}
        game.process_configuration(**kwargs)
        self.assertTrue(game.log_level == logging.INFO)

        kwargs = {"log_level": "warning"}
        game.process_configuration(**kwargs)
        self.assertTrue(game.log_level == logging.WARNING)

        kwargs = {"log_level": "error"}
        game.process_configuration(**kwargs)
        self.assertTrue(game.log_level == logging.ERROR)

        kwargs = {"log_level": "critical"}
        game.process_configuration(**kwargs)
        self.assertTrue(game.log_level == logging.CRITICAL)

        # Ensure the process arguments method can handle invalid log levels
        kwargs = {"log_level": "invalid"}
        self.assertRaises(ValueError, game.process_configuration, **kwargs)


    def test_start(self):
        game = Application()
        game.start()
        self.assertTrue(game.running)


    def test_update(self):
        game = Application()
        game.update()
        # Add assertions to check if the game state has been updated correctly


    def test_render(self):
        game = Application()
        game.render()
        # Add assertions to check if the game graphics have been rendered correctly


    def test_quit(self):
        game = Application()
        game.quit()
        # Add assertions to check if the game has been quit correctly


if __name__ == "__main__":
    unittest.main()
    