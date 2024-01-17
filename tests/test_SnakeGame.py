import unittest
from src.SnakeGame.SnakeGame import SnakeGame


class TestSnakeGame(unittest.TestCase):
    def test_process_arguments(self):
        # Ensure that the debug argument is set to False by default
        game = SnakeGame()
        game.process_arguments()
        self.assertTrue(game.debug == False)

        # Ensure that the debug argument is set to True when debug=True is passed as a keyword argument
        kwargs = {"debug": True}
        game.process_arguments(**kwargs)
        self.assertTrue(game.debug == True)

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