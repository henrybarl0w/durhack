import pygame
import game

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poker Game")

# Create a Game instance
game = game.PokerGame()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    game.update()

    # Render the game
    window.fill((0, 128, 0))  # Green background for the poker table
    game.draw(window)
    pygame.display.flip()

# Clean up
pygame.quit()