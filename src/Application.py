import pygame
import logging
import os
import json

from pathlib import Path


# TODO
# Set pygame caption
class Application:
    # Application options
    default_options = {
        "configuration_file": "./res/settings.json",
        "log_level_name": "error",
        "log_level": logging.ERROR,
        "width": 800,
        "height": 600,
    }
        
    options = {
        "configuration_file": None,
        "log_level": None,
        "log_level_name": None,
        "width": None,
        "height": None,

    }

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

        Configuration methods:
            load_configuration(): Processes the arguments passed to the Application object.
            load_configuration_file(): Processes the Application configuration file.

            apply_configuration(): Apply the options passed to the Application object.
            apply_resolution(): Applies the resolution options.
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


    def load_configuration(self, **command_line_arguments):
        """
        Process the Application configuration.

        Returns:
            None

        TODO
        Add to setup.py to put the configuration file in the enviromental variables
        """
        # Priority of configuration options:
        # 1. Command line arguments
        # 2. Enviromental variables
        # 3. Configuration file options
        # 4. Default options

        # 1. Check if configuration_file is a kwarg
        #   1.1 If it is, set the configuration_file attribute to the value of the kwarg
        #   1.2 If it is not, check if the configuration_file is in the enviromental variables
        #       1.2.1 If it is, set the configuration_file attribute to the value of the enviromental variable
        #       1.2.2 If it is not, set the configuration_file attribute to the default configuration file
        # 2. Load the configuration file
        # 3. Iterate over each option in the options attribute
        #   3.1 If the option attribute is in the kwargs, set the option attribute to the value of the kwarg
        #   3.2 If the option attribute is not in the kwargs, check if the option attribute is in the enviromental variables
        #       3.2.1 If it is, set the option attribute to the value of the enviromental variable
        #       3.2.2 If it is not, check if the option attribute already has a value
        #           3.2.3.1 If it does, do nothing
        #           3.2.3.2. If it does not, set the option attribute to the default value
        if "configuration_file" in command_line_arguments:
            self.configuration_file = command_line_arguments["configuration_file"]
        elif "configuration_file" in os.environ:
            self.configuration_file = os.environ["configuration_file"]
        else:
            self.configuration_file = self.DEFAULT_CONFIGURATION_FILE


        self.load_configuration_file()
        self.load_command_line_arguments(**command_line_arguments)


    def load_command_line_arguments(self, **kwargs):
        """
        Process the command line arguments passed to the Application object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        self.apply_options(**kwargs)


    def load_configuration_file(self):
        """
        Process the Application configuration file.

        Args:
            configuration_file (str): The path to the configuration file.

        Returns:
            None

        Raises:
            FileNotFoundError: If the configuration file is not found.
            JSONDecodeError: If the configuration file is not valid JSON.
        """
        configuration_file = Path(self.configuration_file)


        if not configuration_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {configuration_file}")
                

        with open(configuration_file) as file:
            configuration = json.load(file)
            self.apply_options(**configuration)


        self.apply_options(**configuration)


    def apply_options(self, **kwargs):
        """
        Process the Application options.
        """
        for option in self.options:
            if option == "log_level":
                self.apply_log_level(kwargs[option])
            else: 
                self.apply_option(option, **kwargs)

    
    def apply_option(self, option, **kwargs):
        if option in kwargs:
            setattr(self, option, kwargs[option])
        elif option in os.environ:
            setattr(self, option, os.environ[option])
        elif hasattr(self, option) and getattr(self, option) is None:
            setattr(self, option, self.options[option])


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
        valid_log_levels = [
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ]

        if not log_level is None and isinstance(log_level, str) or log_level.upper() not in valid_log_levels:
            raise ValueError(f"Invalid log level: {log_level}")
        

        # Making the log_level_name attribute lowercase allows the log level to be more verbose, 
        # because all uppercase letters look ugly.
        self.apply_option("log_level_name", log_level=log_level.lower())
        self.apply_option("log_level", log_level=getattr(logging, log_level.upper())) # logging.ERROR = 40, logging.DEBUG = 10...


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
