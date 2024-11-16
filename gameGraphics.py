import pygame
import random

pygame.init()

GRID_SIZE = 10
CELL_SIZE = 32
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set player position at the 0,0 left corner
player_pos = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

# Shop and Random Encounter Positions (randomly placed)
shop_pos = pygame.Rect(random.randint(0, GRID_SIZE-1) * CELL_SIZE, random.randint(0, GRID_SIZE-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
encounter_pos = pygame.Rect(random.randint(0, GRID_SIZE-1) * CELL_SIZE, random.randint(0, GRID_SIZE-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)

def handleInteraction():
    if player_pos.colliderect(shop_pos):
        print("You have entered the Shop. Do you want to buy the swashbuckler sword?")
    elif player_pos.colliderect(encounter_pos):
        print("A wild monster randomly appears!")

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


