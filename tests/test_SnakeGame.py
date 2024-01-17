import logging
import unittest
from src.SnakeGame.SnakeGame import SnakeGame


class TestSnakeGame(unittest.TestCase):
    def test_process_arguments(self):
        # Ensure that the debug argument is set to False by default
        game = SnakeGame()
        game.process_arguments()
        self.assertTrue(game.log_level == logging.ERROR)

        # Ensure the process arguments method can handle the log level argument
        kwargs = {"log_level": "debug"}
        game.process_arguments(**kwargs)
        self.assertTrue(game.log_level == logging.DEBUG)

        kwargs = {"log_level": "info"}
        game.process_arguments(**kwargs)
        self.assertTrue(game.log_level == logging.INFO)

        kwargs = {"log_level": "warning"}
        game.process_arguments(**kwargs)
        self.assertTrue(game.log_level == logging.WARNING)

        kwargs = {"log_level": "error"}
        game.process_arguments(**kwargs)
        self.assertTrue(game.log_level == logging.ERROR)

        kwargs = {"log_level": "critical"}
        game.process_arguments(**kwargs)
        self.assertTrue(game.log_level == logging.CRITICAL)

        # Ensure the process arguments method can handle invalid log levels
        kwargs = {"log_level": "invalid"}
        self.assertRaises(ValueError, game.process_arguments, **kwargs)

    def test_start(self):
        game = SnakeGame()
        game.start()
        self.assertTrue(game.running)

    def test_update(self):
        game = SnakeGame()
        game.update()
        # Add assertions to check if the game state has been updated correctly

    def test_render(self):
        game = SnakeGame()
        game.render()
        # Add assertions to check if the game graphics have been rendered correctly

    def test_quit(self):
        game = SnakeGame()
        game.quit()
        # Add assertions to check if the game has been quit correctly


if __name__ == "__main__":
    unittest.main()