import pygame
import logging
import os
import json

from pathlib import Path
import pygame
import logging
import os
import json
import sys
from pathlib import Path
import argparse
# TODO
# Set pygame caption
class Application:
    # Configurable options
    configuration_file = None
    log_level = getattr(logging, "DEBUG") # logging.ERROR = 40, logging.DEBUG = 10...
    log_level_name = "debug"
    width = None
    height = None



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

        Options:
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
        self.setup()


    def setup(self):
            """
            Sets up the Application.

            This method loads the options (log_level, width, height, configuration_file) on startup
            using the following priority:
            1. Command line arguments
            2. Environmental variables
            3. Configuration file
            4. Default values

            Returns:
                None
            """
            # Parse command line arguments
            parser = argparse.ArgumentParser()
            parser.add_argument("--log-level", dest="log_level", choices=["debug", "info", "warning", "error", "critical"], help="The log level to be set.")
            parser.add_argument("--width", dest="width", type=int, help="The width of the game window.")
            parser.add_argument("--height", dest="height", type=int, help="The height of the game window.")
            parser.add_argument("--config-file", dest="configuration_file", help="The path to the configuration file.")
            args = parser.parse_args()

            # Load options from command line arguments
            if args.log_level:
                self.log_level = getattr(logging, args.log_level.upper(), logging.DEBUG)
                self.log_level_name = args.log_level.lower()
            if args.width:
                self.width = args.width
            if args.height:
                self.height = args.height
            if args.configuration_file:
                self.configuration_file = args.configuration_file

            # Load options from environmental variables
            if "LOG_LEVEL" in os.environ:
                self.log_level = getattr(logging, os.environ["LOG_LEVEL"].upper(), logging.DEBUG)
                self.log_level_name = os.environ["LOG_LEVEL"].lower()
            if "WIDTH" in os.environ:
                self.width = int(os.environ["WIDTH"])
            if "HEIGHT" in os.environ:
                self.height = int(os.environ["HEIGHT"])
            if "CONFIGURATION_FILE" in os.environ:
                self.configuration_file = os.environ["CONFIGURATION_FILE"]

            # Load options from configuration file
            if self.configuration_file:
                with open(self.configuration_file) as f:
                    config = json.load(f)
                    self.log_level = getattr(logging, config.get("log_level", self.log_level_name.upper()), logging.DEBUG)
                    self.log_level_name = config.get("log_level_name", self.log_level_name.lower())
                    self.width = config.get("width", self.width)
                    self.height = config.get("height", self.height)

            # Set default values if options are still None
            if self.log_level is None:
                self.log_level = getattr(logging, "DEBUG")
            if self.log_level_name is None:
                self.log_level_name = "debug"
            if self.width is None:
                self.width = 800
            if self.height is None:
                self.height = 600

            # Continue with the rest of the setup process
            self.setup_logging()
            self.setup_pygame()


    def setup_pygame(self):
        """
        Set up the Pygame library for the game.

        Returns:
            None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
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
