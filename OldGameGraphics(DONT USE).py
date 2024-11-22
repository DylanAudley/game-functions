import pygame
import random
import time
from gamefunctions import new_random_monster, print_shop_menu


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

# Player class to encapsulate all player data
class Player:
    def __init__(self):
        self.health = 100
        self.gold = 10
        self.equipped_items = []
        self.item_inventory = [
            {'name': 'swashbuckler sword', 'type': 'weapon', 'minDurability': 1, 'currentDurability': 25, 'attackBoost': 10},
            {'name': 'milkshake', 'type': 'healthBoost', 'healthRestore': 10, 'quantity': 3}
        ]

    def buy_item(self, item_name, cost):
        """
        Buy an item if the player has enough gold. 
        Adds the item to the inventory or equipment list accordingly.
        """
        if self.gold >= cost:
            self.gold -= cost
            if item_name == 'Swashbuckler Sword':
                self.equipped_items.append('Swashbuckler Sword')
            elif item_name == 'Milkshake':
                for item in self.item_inventory:
                    if item['name'] == 'milkshake':
                        item['quantity'] += 1
                        break
            print(f"Purchased {item_name}!")
        else:
            print(f"Not enough gold to purchase {item_name}.")

    def restore_health(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100  # Cap health at 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

# Initialize player
player = Player()

#Set player position at the 0,0 left corner
player_pos = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

# Shop and Random Encounter Positions (randomly placed)
shop_pos = pygame.Rect(random.randint(0, GRID_SIZE-1) * CELL_SIZE, random.randint(0, GRID_SIZE-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
encounter_pos = pygame.Rect(random.randint(0, GRID_SIZE-1) * CELL_SIZE, random.randint(0, GRID_SIZE-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)

# Variable to track whether or not player has already encountered a random monster, fix for non-stop random monsters
monsterEncounter = False
# Same variable method for the shop
shopEncounter = False
# message displayed on graphics screen when encounting monster 
encounterMessage = ""

# Store the time when the interaction message is triggered
interactionMessageTime = None
interactionMessageDuration = 3  # Message will stay for 3 seconds

def handleInteraction():
    """
    Handles interactions when the player collides with the shop or random encounter.
    If the player moves to the shop's location, a shop interaction message is displayed.
    If the player moves to the random encounter's location, a random monster encounter message is displayed.
    
    Returns:
        str: The interaction message to be displayed on screen.
    """
    global monsterEncounter, shopEncounter, encounterMessage, interactionMessageTime
    
    if player_pos.colliderect(shop_pos) and not shopEncounter:
        print("You have entered the Shop. Press '1' to buy Swashbuckler Sword (5.99), '2' to buy Milkshake (3.50), '3' to Exit shop.")
        print_shop_menu('Swashbuckler Sword', 5.99, 'Milkshake', 3.50)
        shopEncounter = True

    elif player_pos.colliderect(encounter_pos) and not monsterEncounter:
        print("A wild monster randomly appears!")
        monster = new_random_monster()
        print(f"Monster Name: {monster['name']}")
        print(f"Description: {monster['description']}")
        print(f"Health: {monster['health']}, Power: {monster['power']}, Money: {monster['money']}")
        
        if player.health > 0:
            player.take_damage(monster['power'])
            print(f"You took damage! Current health: {player.health}")
            if player.health <= 0:
                print("You have been defeated!")

        encounterMessage = f"Encountered {monster['name']}! Health: {monster['health']}"
        monsterEncounter = True

        # Start the timer for the encounter message
        interactionMessageTime = time.time()  # Trigger the timer when the encounter happens
            
        return encounterMessage
    
    return None

def drawGrid():
    """
    Draws the 10x10 grid on the screen. Each cell is 32x32 pixels.
    This grid serves as the background to show the player's movement on the grid.

    Returns: None
    """
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), 1)

def drawGameElements():
    """
    Draws the player (blue square), shop (green circle), and random encounter (red circle)
    on the screen at their respective positions.

    Returns: None
    """
    # Draw player (blue square)
    pygame.draw.rect(screen, (0, 0, 255), player_pos)

    # Draw shop (green circle)
    pygame.draw.circle(screen, GREEN, shop_pos.center, CELL_SIZE // 2)

    # Draw random encounter (red circle)
    pygame.draw.circle(screen, RED, encounter_pos.center, CELL_SIZE // 2)

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
            elif player_pos.colliderect(shop_pos):
                itemShop()
            #     player.buy_item('Swashbuckler Sword', 5.99)
            # elif event.key == pygame.K_2 and player_pos.colliderect(shop_pos) and not shopEncounter:
            #     player.buy_item('Milkshake', 3.50)
            # elif event.key == pygame.K_3 and player_pos.colliderect(shop_pos) and not shopEncounter:
            #     print("You have exited the shop.")
            #     shopEncounter = True # Preventing bugs

    interactionMessage = handleInteraction()

    # Display interaction message (if any)
    if interactionMessage:
        draw_text(interactionMessage, (10, 10))  # Draw text at the top left

    draw_text(f"Health: {player.health}", (10, 40))
    draw_text(f"Gold: {player.gold:.2f}", (10, 70))
    draw_text(f"Inventory: {', '.join(player.equipped_items) if player.equipped_items else 'None'}", (10, 100))

    # If the player is on the monster encounter area, display the encounter message
    if encounterMessage:
        draw_text(encounterMessage, (10, 130))  # Display monster encounter message

    pygame.display.flip() # Update display

    pygame.time.Clock().tick(10) # Frame rate (FPS)


pygame.quit() # Guit game failsafe 


