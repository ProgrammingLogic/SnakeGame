import pygame

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
        self.setup_pygame()
        self.start()


    def process_arguments(self, *args, **kwargs):
        # Process arguments
        if "debug" in kwargs:
            self.debug = kwargs["debug"]
        else:
            self.debug = False


    def start(self):
        """
        Starts the game logic.

        This method sets the `running` attribute to True, indicating that the game is running.
        """
        self.running = True


    def setup_pygame(self):
        # Setup pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()


    def loop(self):
        # Game loop
        while self.running:
            self.update()
            self.render()

            # Limit the game to 60 FPS
            self.clock.tick(60)


    def quit(self):
        pygame.quit()


    def render(self):
        self.screen.fill("purple")
        pygame.display.flip()


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event detected")
                self.running = False
