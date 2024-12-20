
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game Variables
maps = 11
difficulties = ["Easy", "Medium", "Hard", "Insane"]
blob_types = ["Fire", "Water", "Thunder", "Steel", "Plant", "Ice", "Telekinesis", "Dragon", "Rock"]

# Function to load maps (Placeholder)
def load_map(map_number):
    print(f"Loading map {map_number}")

# Function to set difficulty (Placeholder)
def set_difficulty(difficulty):
    print(f"Setting difficulty to {difficulty}")

# Main Game Loop
def game_loop():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Game logic here

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    # Example: Load the first map and set to Easy difficulty
    load_map(1)
    set_difficulty(difficulties[0])
    game_loop()
