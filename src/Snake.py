from logging import Logger

class Snake:
    """
    The Snake class represents the snake in the game.
    
    Attributes:
        application (Application): The application object.
    """
    application = None
    x = 0
    y = 0


    def __init__(self, application):
        self.application = application
        self.logger = application.logger
        self.logger.debug("Snake initializing.")


        screen_width = self.application.screen.get_width()
        screen_height = self.application.screen.get_height()

        self.x = screen_width / 2
        self.y = screen_height / 2

        self.logger.debug("Snake initialized.")


    def update(self):
        """
        Updates the snake.
        """
        self.x += 2