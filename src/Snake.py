import pygame

from logging import Logger

class Snake(pygame.sprite.Sprite):
    """
    The Snake class represents the snake in the game.
    
    Attributes:
        Sprite Attributes
            speed (tuple): The speed of the snake.

        Pygame Attributes
            rect (pygame.Rect): The rectangle of the snake.
            image (pygame.Surface): The image of the snake.
            screen (pygame.Surface): The screen the snake is in.
            area (pygame.Rect): The area of the scene the snake is in.

        Application Attributes
            application (Application): The application object.
            logger (Logger): The logger object.
    """
    application = None
    logger = None
    speed = (-2, -2) # Speed x, y


    def __init__(self, application, screen, start_position=(0, 0)):
        pygame.sprite.Sprite.__init__(self)

        self.application = application
        self.screen = screen
        self.area = screen.get_rect()
        self.logger = application.logger
        self.logger.debug("Snake initializing.")
        
        # Initilization sprite graphic 
        self.image = pygame.Surface((10, 10))
        self.image.fill("white")
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_position

        self.logger.debug("Snake initialized.")
        

    def update(self):
        """
        Updates the snake.
        """
        new_position = self.rect.move(self.speed)

        # If the snake is outside the screen, move to the other side of the screen
        # 1. If snake.x is larger than screen.width, set snake.x to 0
        # 2. If snake.x is smaller than 0, set snake.x to screen.width
        # 3. If snake.y is larger than screen.height, set snake.y to 0
        # 4. If snake.y is smaller than 0, set snake.y to screen.height
        if not (self.area.contains(new_position)):
            if new_position.x > self.area.width:
                new_position.x = 0
            elif self.rect.x < 0:
                new_position.x = self.area.width

            if new_position.y > self.area.height:
                new_position.y = 0
            elif new_position.y < 0:
                new_position.y = self.area.height

        self.rect = new_position