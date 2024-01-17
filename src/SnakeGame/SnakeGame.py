import pygame

class SnakeGame:
    """
    SnakeGame class represents a snake game.

    Attributes:
        None

    Methods:
        __init__(): Initializes the SnakeGame object.
        start(): Starts the game logic.
        update(): Updates the game state.
        render(): Renders the game graphics.
        handle_input(): Handles user input.
    """
    def __init__(self):
        # Setup pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.start()

    def start(self):
        # Start the game logic here
        pass

    def game_loop(self):
        # Game loop
        while self.running:
            self.update()
            self.render()

            # Limit the game to 60 FPS
            self.clock.tick(60)

        pygame.quit()
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def render(self):
        self.screen.fill("purple")
        pygame.display.flip()
