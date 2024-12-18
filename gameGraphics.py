import pygame
import random
import time

pygame.init()

GRID_SIZE = 10
CELL_SIZE = 32
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
SCREEN_WIDTH = SCREEN_HEIGHT = 320
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FONT_COLOR = (0, 0, 0)  # Color for text (black)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Grid")

# Font setup
font = pygame.font.SysFont("Times New Roman", 12)

# Import monster png files
monster_images = {
    "goblin": pygame.image.load("grin-goblin-HD.png"),
    "troll": pygame.image.load("hairyTroll1.png"),
    "George the Giant": pygame.image.load("golem_col.png")
    }

# Scale images to cell size
for key in monster_images:
    monster_images[key] = pygame.transform.scale(monster_images[key], (CELL_SIZE, CELL_SIZE))

# Player class to encapsulate all player data
class Player:
    def __init__(self):
        self.health = 100
        self.gold = 10
        self.equipped_items = []
        self.in_shop = False  # Track whether the player is in the shop

    def enter_shop(self):
        self.in_shop = True

    def exit_shop(self):
        self.in_shop = False

class WanderingMonster:
    def __init__(self):
        # Randomly pick the monster and characteristics from list
        monsterList = [{'name': 'goblin', 'description': 'A sneaky little guy, grabbing your gold.', 'health': [12, 14, 16], 'power': [1, 2, 3], 'money' : [20, 22, 24]},
                       {'name': 'troll', 'health': [15, 18, 21], 'description' : 'A grumpy bridge troll who has a huge wooden club.', 'power' : [25, 30, 35], 'money' : [8, 10, 12]},
                       {'name' : 'George the Giant', 'description' : 'Typically a gentle giant, but has quite a sensitive temper.', 'health': [1000, 1200, 1400], 'power' : [100, 120, 140], 'money' : [3, 5, 7]}
                       ]

        monster_data = random.choice(monsterList)

        # Randomize the health, power, and money based on the monster's stats in list
        self.name = monster_data['name']
        self.description = monster_data['description']
        self.health = random.choice(monster_data['health'])
        self.attack_power = random.choice(monster_data['power'])
        self.money = random.choice(monster_data['money'])

        # Randomize the monster's position on the grid
        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)
        self.rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def move(self):
        # Randomly move the monster in one of 4 directions, staying within bounds
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if direction == 'UP' and self.y > 0:
            self.y -= 1
        elif direction == 'DOWN' and self.y < GRID_SIZE - 1:
            self.y += 1
        elif direction == 'LEFT' and self.x > 0:
            self.x -= 1
        elif direction == 'RIGHT' and self.x < GRID_SIZE - 1:
            self.x += 1
        
        # Update monster's rectangle position based on the new x, y coordinates
        self.rect.x = self.x * CELL_SIZE
        self.rect.y = self.y * CELL_SIZE

    def check_encounter(self, player_rect):
        # Check if the player is in the same position as the monster
        return self.rect.colliderect(player_rect)

# Doubling monster spawning function
def spawn_monsters(count):
    return [WanderingMonster() for _ in range(count)]

# Initialize player
player = Player()

# Set player position at the 0,0 left corner
player_pos = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

# Spawn initial monsters
monster_count = 1
monsters = spawn_monsters(monster_count)

# Message display timer
encounter_message_time = None

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
    Draws the player (blue square), random encounter (red circle)
    on the screen at their respective positions.
    """
    # Draw player (blue square)
    pygame.draw.rect(screen, (0, 0, 255), player_pos)

    # Draw the monster(s) png files or red circle if no access
    for monster in monsters:
        if monster.name in monster_images:
            screen.blit(monster_images[monster.name], monster.rect.topleft)
        else:
            pygame.draw.circle(screen, RED, (monster.rect.centerx, monster.rect.centery), CELL_SIZE // 2)

def draw_text(text, position):
    """
    Draws the provided text on the screen at the given position.
    
    Args:
        text (str): The text to be drawn on the screen.
        position (tuple): The (x, y) position where the text will be displayed.
        
    Returns:
        None
    """
    text_surface = font.render(text, True, FONT_COLOR)
    screen.blit(text_surface, position)

# Game Loop code
running = True
gameOver = False

while running: 
    screen.fill(WHITE)  # Set background screen as white

    drawGrid()  # Draw grid

    drawGameElements()  # Draw player and random monster encounter

    # Move the monster/monsters randomly
    for monster in monsters:
        monster.move()

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
            elif event.key == pygame.K_m:  # Press M to double monsters
                # Double the number of monsters
                monster_count *= 2  # Double the monster count
                monsters = spawn_monsters(monster_count)  # Spawn new set of monsters
                player.health = 100  # Reset player health
                print("Monsters doubled and health reset!")
        
    # Check if the player has encountered a monster
    for monster in monsters:
        if monster.check_encounter(player_pos):
            player.health -= 10  # Decrease player health by 10
            encounter_message_time = time.time()  # Track the time the encounter happens

    # Display encounter message for a few seconds
    if encounter_message_time:
        elapsed_time = time.time() - encounter_message_time
        if elapsed_time < 3:  # Show message for 3 seconds
            draw_text(f"A wild {monster.name} attacks! You lose 10 HP!", (10, 10))
        else:
            encounter_message_time = None  # Reset encounter message timer

    # Check if the player has died and give options
    if player.health <= 0 and not gameOver:
        message_display_time = time.time()  # Start timer for "Game Over" message
        gameOver = True

    # If game is over, display the "Game Over" message 
    if gameOver:
        elapsed_time = time.time() - message_display_time
        if elapsed_time < 5:  # Show message for 5 seconds
            draw_text("Game Over! Press M to double the monsters, or Q to quit.", (100, 150))
        else:
            draw_text("Press M to double the monsters, or Q to quit.", (100, 150))

    # Display player information
    draw_text(f"Health: {player.health}", (10, 40))
    draw_text(f"Gold: {player.gold:.2f}", (10, 70))
    draw_text(f"Inventory: {', '.join(player.equipped_items) if player.equipped_items else 'None'}", (10, 100))

    # User input quit logic
    if gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False

    pygame.display.flip()  # Update display

    pygame.time.Clock().tick(10)  # Frame rate (FPS)

pygame.quit()  # Quit game failsafe
