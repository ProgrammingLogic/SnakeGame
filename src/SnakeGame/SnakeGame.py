import pygame
import logging

class SnakeGame:
    """
    SnakeGame class represents a snake game.

    Attributes:
        debug (bool): Indicates whether debug mode is enabled.
        running (bool): Indicates whether the game is running.

    Methods:
        __init__(): Initializes the SnakeGame object.
        process_arguments(): Processes the arguments passed to the SnakeGame object.
        start(): Starts the game logic.
        setup_pygame(): Sets up the Pygame library for the game.
        game_loop(): The main game loop.
        quit(): Quits the game.
        render(): Renders the game graphics.
        update(): Updates the game state.
    """

    def __init__(self, *args, **kwargs):
        self.process_arguments(*args, **kwargs)
        self.setup_logging()
        self.setup_pygame()
        self.start()

    def process_arguments(self, *args, **kwargs):
        """
        Process the arguments passed to the SnakeGame object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        # Process arguments
        if "log_level" in kwargs:
            self.process_log_level(kwargs["log_level"])
        else:
            self.log_level = logging.ERROR

    def process_log_level(self, log_level):
        """
        Process the log level argument.

        Args:
            log_level (str): The log level to be set.

        Returns:
            None

        Raises:
            ValueError: If an invalid log level is provided.
        """
        log_levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

        if log_level in log_levels.keys():
            self.log_level = log_levels[log_level]
        else:
            raise ValueError(f"Invalid log level: {log_level}")

    def setup_logging(self):
        """
        Set up logging for the game.

        Returns:
            None
        """
        # Setup logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter and add it to the handler
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(ch)

    def start(self):
        """
        Starts the game logic.

        This method sets the `running` attribute to True, indicating that the game is running.

        Returns:
            None
        """
        self.running = True

    def setup_pygame(self):
        """
        Set up the Pygame library for the game.

        Returns:
            None
        """
        # Setup pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def loop(self):
        """
        The main game loop.

        Returns:
            None
        """
        # Game loop
        while self.running:
            self.update()
            self.render()

            # Limit the game to 60 FPS
            self.clock.tick(60)

    def quit(self):
        """
        Quits the game.

        Returns:
            None
        """
        pygame.quit()

    def render(self):
        """
        Renders the game graphics.

        Returns:
            None
        """
        self.screen.fill("purple")
        pygame.display.flip()

    def update(self):
        """
        Updates the game state.

        Returns:
            None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.logger.info("pygame.QUIT event detected.")
                self.running = False
