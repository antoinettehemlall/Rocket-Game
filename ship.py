import pygame

class Ship:

    def __init__(self, rs_game):
        """Set starting position of ship."""
        self.screen = rs_game.screen
        self.screen_rect = rs_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('images/rocket_image.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        def blitme(self):
            """Draw ship at its current location."""
            self.screen.blit(self.image, self.rect)