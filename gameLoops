from gamefunctions import new_random_monster

itemInventory = [
                 {'name': 'swashbuckler sword', 'type': 'weapon', 'minDurability': 1, 'currentDurability': 25, 'attackBoost': 10},
                 {'name': 'milkshake', 'type': 'healthBoost', 'healthRestore': 10, 'quantity': 3},
                 {'name': 'magic potion', 'type': 'potion', 'effect': 'Defeats any one monster without losing HP.', 'quantity': 1}
                ]

def main():
    """
    Main function to start the game. It generates a random monster,
    displays its information, and enters a loop where the player can
    interact with the monster by fighting, sleeping to restore health,
    or quitting the game.
    """
    
    # Generate a random monster
    monster = new_random_monster()
    print(f'A wild {monster["name"]} appears!')
    print(f'Description: {monster["description"]}')
    print(f'Health: {monster["health"]}')
    print(f'Power: {monster["power"]}')
    print(f'Money: {monster["money"]}')

    playerHealth = 100  # Set players base health
    playerGold = 10  # Set player's gold 
    equippiedItems = [] # Set list to keep track of items
    playerAttackPower = 10  # Default attack power
    swordDurability = itemInventory[0]['currentDurability']  # Set initial sword durability
    monsterDefeated = False # Sets a variable to determine if the monster has already been killed i.e Magic Potion

    while True:
        displayMenu(monster, playerHealth, playerGold, equippiedItems, monsterDefeated)

        choice = input('Enter your choice (1-5): ')
        if choice == '1' and not monsterDefeated:
            playerHealth = fightMonster(monster, playerHealth, playerAttackPower)
            if playerHealth <= 0: # Check if player has HP
                print('Game Over!')
                break 
            swordDurability -= 1 # Reduce durability after fighting
            if swordDurability <= 0: # Check if sword is broken
                print("Your sword has broken!")
                equippiedItems.remove('swashbuckler sword')

        elif choice == '2':
            if playerGold >= 5:  # Check if the player has enough money
                playerHealth += 15  # Restore 15 HP
                playerGold -= 5  # Deduct 5 gold
                playerHealth = min(playerHealth, 100)  # Cap health at 100
                print(f'You slept and restored 15 HP (Unless you already had 100 HP... you gotta read carefully!) Current HP: {playerHealth}. Current Gold: {playerGold}.')
            else:
                print('Not enough gold to sleep!')

        elif choice == '3':  # Equip items
            playerHealth, playerAttackPower, swordDurability = equipItems(
                itemInventory, equippiedItems, playerHealth, playerAttackPower, swordDurability)

        
        elif choice == '4': 
            potion = next((item for item in itemInventory if item['name'] == 'magic potion'), None)
            if potion and potion['quantity'] > 0 and not monsterDefeated:
                print(f"You use a magic potion and defeat the {monster['name']} without losing HP!")
                potion['quantity'] -= 1
                monsterDefeated = True
            else:
                print("You have no magic potions to use or the monster has already been defeated!")

        elif choice == '5':
            print('You chose to quit. Goodbye!!')
            break

        else:
            print('Invalid choice. Please choose (1-5).')

def displayMenu(monster, playerHealth, playerGold, equippiedItems, monsterDefeated):
    """
    Displays the current status of the player and the available options.

    Parameters:
        monster (dict): The current monster with its attributes.
        playerHealth (int): The player's current health.
        playerGold (int): The player's current gold.
        equippiedItems (list): The items the player has equipped.

    Returns:
        None
    """
    print(f'Current HP: {playerHealth}, Current Gold: {playerGold}')
    print('Equipped items:', ', '.join(equippiedItems) if equippiedItems else 'None')
    print('What would you like to do?')
    print("1) Fight Monster" if not monsterDefeated else "1) Monster already defeated, cannot fight")
    print("2) Sleep (Restore 15 HP for 5 Gold, but remember HP caps out at 100)")
    print("3) Choose an item from inventory to equip")
    print("4) Use your magic potion (Defeat monster without losing HP)"if not monsterDefeated else "4) Monster Already Defeated")
    print("5) Quit")

def fightMonster(monster, playerHealth, playerAttackPower):
    """
    Simulates a fight between the player and the monster.

    Parameters:
        monster (dict): The current monster with its attributes.
        playerHealth (int): The player's current health.
        playerAttackPower (int): The player's current attack power.

    Returns:
        int: The updated player's health after the fight.
    """
        
    while monster["health"] > 0 and playerHealth > 0:
        print(f'You attack the {monster["name"]}!')
        monster["health"] -= playerAttackPower
        print(f'The {monster["name"]} has {monster["health"]} left!')
        
        if monster["health"] <= 0: # Check if monster has HP 
            print(f"You defeated the {monster['name']}!")
            break
        
        playerHealth -= monster["power"] # Reduce player health by monster attack power
        print(f'The {monster["name"]} attacks back! You have {playerHealth} HP left!')

        if playerHealth <= 0: # Check if player has HP 
            print(f'The {monster["name"]} killed you!')
            break
    
    return playerHealth  # Returns updated player health after the fight

def equipItems(itemInventory, equippiedItems, playerHealth, playerAttackPower, swordDurability):
    """
    Allows the player to equip items from the inventory.

    Parameters:
        itemInventory (list): The list of items available for equipping.
        equippedItems (list): The list of items the player has currently equipped.
        playerHealth (int): The player's current health.
        playerAttackPower (int): The player's current attack power.
        swordDurability (int): Current durability of the sword.

    Returns:
         tuple: Updated playerHealth, playerAttackPower, and swordDurability.
    """

    print("\nAvailable items to equip:")
    for index, item in enumerate(itemInventory):
        if item['type'] != 'potion':  # Only show equipable items
            print(f"{index + 1}: {item['name']}")
        
    while True:
        choice = input('Enter the number of the item you would like to equip or type "done" to exit: ')
    
        if choice.lower() == 'done':
            break
        
        if choice.isdigit():
            choice_index = int(choice) - 1
            
            if 0 <= choice_index < len(itemInventory):
                item = itemInventory[choice_index]
                if item['type'] == 'healthBoost':
                    if item['quantity'] > 0:  # Check if there is quantity available
                        playerHealth += item['healthRestore'] # Add 10 HP 
                        item['quantity'] -= 1  # Reduce the quantity
                        playerHealth = min(playerHealth, 100)  # Cap health at 100
                        equippiedItems.append(item['name'])
                        print(f"You equipped {item['name']} for {item['healthRestore']} HP! (Unless you already had 100 HP :)")
                    else:
                        print('You are out of milkshakes, please choose something else or "done".')
                elif item['type'] == 'weapon':
                    if swordDurability > 0:
                        playerAttackPower += item['attackBoost']
                        equippiedItems.append(item['name'])
                        print(f"You equipped {item['name']} and gained {item['attackBoost']} attack power!")
                    else:
                        print(f"Cannot equip {item['name']}: durability too low.")
                
            else:
                print("Invalid choice, please try again.")
        else:
            print("Please enter a valid number or 'done'.")

    return playerHealth, playerAttackPower, swordDurability  # Updated values

if __name__ == '__main__':
    main()