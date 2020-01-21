import pygame
import sys
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()
