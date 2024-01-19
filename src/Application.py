import pygame
import logging
import os
import json

from pathlib import Path


class Application:
    # Final variables
    DEFAULT_LOG_LEVEL = logging.ERROR

    # Configuration variables
    log_level = None

    # Instance variables
    logger = None
    running = False
    screen = None
    clock = None
    """
    Application class represents a snake game.

    Attributes:
        Instance variables:
            logger (logging.Logger): The logger object for the Application class.
            running (bool): Indicates whether the game is running.
            screen (pygame.Surface): The screen to be used for the game.
            clock (pygame.time.Clock): The clock to be used for the game.

        Configuration variables:
            log_level (int): The log level to be set.

        Final variables:
            DEFAULT_LOG_LEVEL (int): The default log level to be set.

    Methods:
        General Application methods:
            __init__(): Initializes the Application object.

            setup(): Sets up the Application.
            setup_logging(): Sets up logging for the game.

            start(): Starts the Application.
            stop(): Stops the Application.

        Configuration methods:
            load_configuration(): Processes the arguments passed to the Application object.
            load_configuration_file(): Processes the Application configuration file.

            apply_configuration(): Apply the options passed to the Application object.
            apply_log_level(): Applies the log level option.

        Game methods:
            setup_pygame(): Sets up the Pygame library for the game.
            
            loop(): The main game loop.
            render(): Renders the game graphics.
            update(): Updates the game state.
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
        self.load_configuration(*args, **kwargs)
        self.setup()


    def load_configuration(self, *args, **kwargs):
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
            self.load_configuration_file(kwargs["configuration_file"])
        elif "configuration_file" in os.environ:
            self.load_configuration_file(os.environ["configuration_file"])

        self.apply_configuration(*args, **kwargs)


    def load_configuration_file(self, configuration_file):
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
                self.apply_configuration(**configuration)
        else:
            raise FileNotFoundError(f"Configuration file not found: {configuration_file}")


    def apply_configuration(self, *args, **kwargs):
        """
        Apply the specified configuration options.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        self.apply_log_level(kwargs["log_level"])


    def apply_log_level(self, log_level):
        """
        Applies the log level option.

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


    # Setup methods
    def setup(self):
        """
        Sets up the Application.

        Returns:
            None
        """
        self.setup_logging()
        self.setup_pygame()


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


    def setup_pygame(self):
        """
        Set up the Pygame library for the game.

        Returns:
            None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()


    # Start methods
    def start(self):
        """
        Starts the Application.

        This method sets the `running` attribute to True, indicating that the Application is running.

        Returns:
            None
        """
        self.running = True


    # Stop methods
    def stop(self):
        """
        Stops the Application.

        Returns:
            None
        """
        pygame.quit()


    # Game loop methods
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
