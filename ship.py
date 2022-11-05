import pygame

class Ship:

    def __init__(self, rs_game):
        """Set starting position of ship."""
        self.screen = rs_game.screen
        self.settings = rs_game.settings
        self.screen_rect = rs_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('images/rocket_image.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # update rect object from positon attributes.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)