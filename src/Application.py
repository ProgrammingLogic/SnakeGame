import pygame
import logging
import os
import json

from pathlib import Path


class Application:
    DEFAULT_LOG_LEVEL = logging.ERROR

    """
    Application class represents a snake game.

    Attributes:
        running (bool): Indicates whether the game is running.
        log_level (int): The log level to be set.
        DEFAULT_LOG_LEVEL (int): The default log level to be set.

    Methods:
        __init__(): Initializes the Application object.
        process_arguments(): Processes the arguments passed to the Application object.
        start(): Starts the game logic.
        setup_pygame(): Sets up the Pygame library for the game.
        game_loop(): The main game loop.
        quit(): Quits the game.
        render(): Renders the game graphics.
        update(): Updates the game state.
        process_log_level(): Processes the log level argument.
        setup_logging(): Sets up logging for the game.
        process_configuration(): Processes the arguments passed to the Application object.
        process_configuration_file(): Processes the Application configuration file.
        process_snake_game_configuration(): Processes the Application configuration.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the Application object.

        kwargs:
            configuration_file (str): The path to the configuration file.
            log_level (str): The log level to be set.
                Valid options are: debug, info, warning, error, and critical

        Returns:
            None
        """
        self.process_configuration(*args, **kwargs)
        self.setup_logging()
        self.setup_pygame()
        self.start()


    def process_configuration(self, *args, **kwargs):
        """
        Process the Application configuration.

        Returns:
            None
        """
        # Load the configuration file prior to processing the command line arguments
        # This allows the command line arguments to override the configuration file
        # TODO
        # Add to setup.py to put the configuration file in the enviromental variables
        if "configuration_file" in kwargs:
            self.process_configuration_file(kwargs["configuration_file"])
        elif "configuration_file" in os.environ:
            self.process_configuration_file(os.environ["configuration_file"])

        self.process_arguments(*args, **kwargs)


    def process_configuration_file(self, configuration_file):
        """
        Process the Application configuration file.

        Args:
            configuration_file (str): The path to the configuration file.

        Returns:
            None

        Raises:
            FileNotFoundError: If the configuration file is not found.
        """
        configuration_file = Path(configuration_file)
                
        if configuration_file.exists():
            with open(configuration_file) as file:
                configuration = json.load(file)
                self.process_arguments(**configuration)
        else:
            raise FileNotFoundError(f"Configuration file not found: {configuration_file}")


    def process_arguments(self, *args, **kwargs):
        """
        Process the arguments passed to the Application object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        self.process_log_level(kwargs["log_level"])


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
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "critical": logging.CRITICAL,
        }

        if log_level is None:
            self.log_level = self.DEFAULT_LOG_LEVEL
        elif not log_level in log_levels.keys():
            raise ValueError(f"Invalid log level: {log_level.lower()}")
        else:
            self.log_level = log_levels[log_level]   


    def setup_logging(self):
        """
        Set up logging for the game.

        Returns:
            None
        """
        # Setup logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

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
