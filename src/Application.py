import pygame
import logging
import os
import json

from pathlib import Path
from argparse import Namespace
 
# TODO
# Set pygame caption
class Application:
    """
    Application class represents a snake game.

    Attributes:
        Instance variables:
            logger (logging.Logger): The logger object for the Application class.
            running (bool): Indicates whether the game is running.
            screen (pygame.Surface): The screen to be used for the game.
            clock (pygame.time.Clock): The clock to be used for the game.

        Options:
            command_line_arguments (argparse.Namespace): The command line arguments passed to the Application.
            configuration_file (str): The path to the configuration file.
            log_level (int): The log level to be set.
            log_level_name (str): The name of the log level to be set.
            width (int): The width of the game window.
            height (int): The height of the game window.

        Final variables:
            DEFAULT_LOG_LEVEL (str): The default log level to be set.

    Methods:
        General Application methods:
            __init__(): Initializes the Application object.

            setup(): Sets up the Application.
            setup_logging(): Sets up logging for the game.

            start(): Starts the Application.
            stop(): Stops the Application.

        Game methods:
            setup_pygame(): Sets up the Pygame library for the game.
            
            loop(): The main game loop.
            render(): Renders the game graphics.
            update(): Updates the game state.
    
    TODO
    Set pygame caption
    """
    # Configurable options
    configuration_file = None
    log_level = getattr(logging, "DEBUG") # logging.ERROR = 40, logging.DEBUG = 10...
    log_level_name = "debug"
    log_directory = None
    log_file = None
    width = None
    height = None


    # Instance variables
    logger = None
    running = False
    screen = None
    clock = None
    
    def __init__(self, command_line_arguments, *args, **kwargs):
        """
        Initializes the Application object.

        Args:
            command_line_arguments (argparse.Namespace or dict): The command line arguments passed to the Application.
            
        kwargs:
            configuration_file (str): The path to the configuration file.
            log_level (str): The log level to be set.
                Valid options are: debug, info, warning, error, and critical

        Returns:
            None
        """
        if isinstance(command_line_arguments, Namespace):
            command_line_arguments = vars(command_line_arguments)
            
        self.command_line_arguments = command_line_arguments
        self.configure()
        self.setup_logging()
        self.setup_pygame()
        

    def configure(self):
        """
        Configures the Application.

        This method loads the options (log_level, width, height, configuration_file) on startup
        using the following priority:
        1. Command line arguments
        2. Environmental variables
        3. Configuration file
        4. Default values

        Returns:
            None
        """
        if "configuration_file" in self.command_line_arguments:
            self.configuration_file = self.command_line_arguments["configuration_file"]
        elif "CONFIGURATION_FILE" in os.environ:
            self.configuration_file = os.environ["CONFIGURATION_FILE"]
        else:
            self.configuration_file = None


        self.load_command_line_arguments()
        self.load_environmental_variables()
        self.load_configuration_file()
        self.set_default_values()


    def load_configuration_file(self):
        """
        Loads the configuration file.

        Returns:
            None
        """
        if self.configuration_file:
            with open(self.configuration_file) as f:
                config = json.load(f)
                self.log_level = getattr(logging, config.get("log_level", self.log_level_name.upper()), logging.DEBUG)
                self.log_level_name = config.get("log_level_name", self.log_level_name.lower())
                self.log_directory = config.get("logging_directory", self.logging_directory)
                self.log_file = config.get("log_file", self.log_file)
                self.width = config.get("width", self.width)
                self.height = config.get("height", self.height)


    def load_environmental_variables(self):
        """
        Loads the environmental variables.

        Returns:
            None
        """
        if "LOG_LEVEL" in os.environ:
            self.log_level = getattr(logging, os.environ["LOG_LEVEL"].upper(), logging.DEBUG)
            self.log_level_name = os.environ["LOG_LEVEL"].lower()
        if "LOG_DIRECTORY" in os.environ:
            self.log_directory = os.environ["LOG_DIRECTORY"]
        if "LOG_FILE" in os.environ:
            self.log_file = os.environ["LOG_FILE"]
        if "WIDTH" in os.environ:
            self.width = int(os.environ["WIDTH"])
        if "HEIGHT" in os.environ:
            self.height = int(os.environ["HEIGHT"])


    def load_command_line_arguments(self):
        """
        Loads the command line arguments.

        Returns:
            None
        """
        args = self.command_line_arguments

        if "log_level" in args and args["log_level"] is not None:
            self.log_level = getattr(logging, args["log_level"].upper())
            self.log_level_name = args["log_level"].lower()
        if "log_directory" in args and args["log_directory"] is not None:
            self.log_directory = args["log_directory"]
        if "log_file" in args and args["log_file"] is not None:
            self.log_file = args["log_file"]
        if "width" in args and args["width"] is not None:
            self.width = args["width"]
        if "height" in args and args["height"] is not None:
            self.height = args["height"]


    def set_default_values(self):
        """
        Sets default values for the options.

        Returns:
            None
        """
        if self.log_level is None:
            self.log_level = getattr(logging, "DEBUG")
        if self.log_level_name is None:
            self.log_level_name = "debug"
        if self.log_directory is None:
            self.log_directory = "logs"
        if self.log_file is None:
            self.log_file = "application.log"
        if self.width is None:
            self.width = 800
        if self.height is None:
            self.height = 600


    def setup_pygame(self):
        """
        Set up the Pygame library for the game.

        Returns:
            None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()


    def setup_logging(self):
        """
        Sets up logging for the game.

        Returns:
            None
        """
        # Set up logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

        # Set up logging formatter
        formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

        # Set up logging file handler
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        if not os.path.exists(f"""{self.log_directory}/application.log"""):
            Path(f"""{self.log_directory}/application.log""").touch()

        file_handler = logging.FileHandler(f"""{self.log_directory}/{self.log_file}""")
        file_handler.setFormatter(formatter)

        # Set up logging stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        # Log the log level
        self.logger.info(f"Log level set to {self.log_level_name.upper()}.")


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
