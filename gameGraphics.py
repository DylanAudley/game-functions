import pygame
import random

pygame.init()

GRID_SIZE = 10
CELL_SIZE = 32
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 320
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set player position at the 0,0 left corner
player_pos = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

# Shop and Random Encounter Positions (randomly placed)
shop_pos = pygame.Rect(random.randint(0, GRID_SIZE-1) * CELL_SIZE, random.randint(0, GRID_SIZE-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
encounter_pos = pygame.Rect(random.randint(0, GRID_SIZE-1) * CELL_SIZE, random.randint(0, GRID_SIZE-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)

def handleInteraction():
    """
    Handles interactions when the player square collides with the shop or random encounter.
    If the player moves to the shop's location, a shop interaction message is displayed.
    If the player moves to the random encounter's location, a random encounter message is displayed.
    """
    if player_pos.colliderect(shop_pos):
        print("You have entered the Shop. Do you want to buy the swashbuckler sword?")
    elif player_pos.colliderect(encounter_pos):
        print("A wild monster randomly appears!")
    
def drawGrid():
    """
    Draws the 10x10 grid on the screen. Each cell is 32x32 pixels.
    This grid serves as the background to show the player's movement on the grid.
    """
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), 1)

def drawGameElements():
    """
    Draws the player (blue square), shop (green circle), and random encounter (red circle)
    on the screen at their respective positions.
    """
    # Draw player (blue square)
    pygame.draw.rect(screen, (0, 0, 255), player_pos)

    # Draw shop (green circle)
    pygame.draw.circle(screen, GREEN, shop_pos.center, CELL_SIZE // 2)

    # Draw random encounter (red circle)
    pygame.draw.circle(screen, RED, encounter_pos.center, CELL_SIZE // 2)

#Game Loop code
running = True
while running: 
    screen.fill(WHITE) #Set background screen as white

    drawGrid() # Draw grid

    drawGameElements() # Draw player, shop, and random monster encounter
    
    # Code handling keyboard interaction with player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_UP and player_pos.top > 0:
                player_pos.move_ip(0, -CELL_SIZE)  # Move up
            elif event.key == pygame.K_DOWN and player_pos.bottom < WINDOW_SIZE:
                player_pos.move_ip(0, CELL_SIZE)  # Move down
            elif event.key == pygame.K_LEFT and player_pos.left > 0:
                player_pos.move_ip(-CELL_SIZE, 0)  # Move left
            elif event.key == pygame.K_RIGHT and player_pos.right < WINDOW_SIZE:
                player_pos.move_ip(CELL_SIZE, 0)  # Move right

    handleInteraction() # Call in interactions with shop and rand monster

    pygame.display.flip() # Update display

    pygame.time.Clock().tick(10) # Frame rate (FPS)


pygame.quit() # Guit game failsafe 


