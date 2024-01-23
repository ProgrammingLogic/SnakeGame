import unittest

from unittest.mock import MagicMock

from src.Application import Application
from src.Snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        command_line_arguments = {
            "log_level": "debug",
            "log_level_name": "DEBUG",
            "log_directory": "logs",
            "log_file": "snake.log",
            "width": 800,
            "height": 600
        }


        self.application = Application(command_line_arguments)
        self.snake = Snake(self.application)


    def test_initialization(self):
        self.assertEqual(self.snake.application, self.application)
        self.assertEqual(self.snake.position[0], self.application.screen.get_width() / 2) # Snake.position.x
        self.assertEqual(self.snake.position[1], self.application.screen.get_height() / 2) # Snake.position.y


    def test_update(self):
        initial_x = self.snake.x
        self.snake.update()
        self.assertEqual(self.snake.x, initial_x + 2)


if __name__ == "__main__":
    unittest.main()