#Dylan Audley
#Adventure Functions
#09/24/2024

""" This is the main module for my gamefunctions. 
    This is the file I started with, and where all of the main functions and output codes will be.
    The purpose of this module is to help me learn python. 
"""


#Function that takes the price of an item, the amount of money you start with and how many you want to purchase and returns how many items you were able to purchase and the amount of money you have leftover.

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
  """ Calculates the number of items purchased and the leftover money.
      
      Args:
        itemPrice: The price of each item.
        startingMoney: The initial amount of money.
        quantityToPurchase: The desired quantity of items to purchase (default: 1).

      Returns:
        A tuple containing the number of items purchased and the leftover money.
  """

    num_purchased = int((startingMoney/itemPrice)-quantityToPurchase)
    leftover_money = (startingMoney - (itemPrice * quantityToPurchase))
    return (num_purchased, leftover_money)

num_purchased, leftover_money = purchase_item(2, 24, 6)
print('You were able to purchase:',num_purchased,'items.')
print('You have ${} afterwards.'.format(leftover_money))

num_purchased, leftover_money = purchase_item(3, 15, 4)
print('You were able to purchase:',num_purchased,'items.')
print('You have ${} afterwards.'.format(leftover_money))

num_purchased, leftove_money = purchase_item(1.5, 18, 9)
print('You were able to purchase:',num_purchased,'items.')
print('You have ${} afterwards.'.format(leftover_money))


#Function that uses random to choose a monster from a dictionary list and outputs that monster and all of its attributes, 3 of which are also randomized each time.

import random

def new_random_monster():
   """Chooses a random monster from a predefined list of monsters, each with unique traits.

    Each monster has different attributes, such as health, power, and money, which are randomly selected from predefined ranges.

    Args:
        None

    Returns:
        dict: A dictionary containing the chosen monster's traits, including:
            - 'name' (str): The name of the monster.
            - 'description' (str): A brief description of the monster.
            - 'health' (int): The monster's health value, randomly selected from the defined range.
            - 'power' (int): The monster's power value, randomly selected from the defined range.
            - 'money' (int): The amount of money the monster carries, randomly selected from the defined range.

    Example:
        >>> monster = new_random_monster()
        >>> print(monster['name'])
        'goblin'  # Output will vary
    """

    monsterList = [{'name': 'goblin', 'description': 'A sneaky little guy, grabbing your gold.', 'health': [8, 10, 12], 'power': [1, 2, 3], 'money' : [20, 22, 24]},
                   {'name': 'troll', 'health': [15, 18, 21], 'description' : 'A grumpy bridge troll who has a huge wooden club.', 'power' : [25, 30, 35], 'money' : [8, 10, 12]},
                   {'name' : 'George the Giant', 'description' : 'The gentlest giant of the land, but quite a sensitive fella.', 'health': [1000, 1200, 1400], 'power' : [100, 120, 140], 'money' : [3, 5, 7]}]

    monster = random.choice(monsterList)
    monster['health'] = random.choice(monster['health'])
    monster['power'] = random.choice(monster['power'])
    monster['money'] = random.choice(monster['money'])

    return monster

monster = new_random_monster()
print('Name:',monster['name'])
print('Description:',monster['description'])
print('Health:',monster['health'])
print('Power:',monster['power'])
print('Money:',monster['money'])


#Function that prints a welcome message for 3 names, which is centered and in single quotes. 


def print_welcome(name, width=20):
  """Prints a welcome message for the given name, centered within a specified width.

    Args:
        name (str): The name of the person to welcome.
        width (int, optional): The total width of the output message. Defaults to 20.

    Returns:
        None: This function does not return a value; it prints the welcome message directly.

    Example:
        >>> print_welcome('Jeff')
        Hello, Jeff!    # Output is centered in a width of 20
  """

  messageCentered = f"{'Hello, ' + name + '!':^{20}}"
  print(messageCentered)
  return None

print_welcome('Jeff')
print_welcome('Audrey', 30)
print_welcome('Ludacris', 15)


#Function that prints a shop menu with the correct alligments, decimal counts, and border format

def print_shop_menu(item1_name, item1_price, item2_name, item2_price):
  """Prints a formatted menu with two items and their prices.

    This function creates a visually appealing menu layout that displays the names and prices
    of two items, aligning them properly for readability.

    Args:
        item1_name (str): The name of the first item.
        item1_price (float): The price of the first item.
        item2_name (str): The name of the second item.
        item2_price (float): The price of the second item.

    Returns:
        None: This function does not return a value; it prints the menu directly.

    Example:
        >>> print_shop_menu('Apple', 3.99, 'Orange', 2.50)
        /----------------------\
        | Apple                $3.99  |
        | Orange               $2.50  |
        \----------------------/
    """

  # Format the prices with two decimal places and a dollar sign
  formatted_price1 = f'${item1_price:.2f}'
  formatted_price2 = f'${item2_price:.2f}'

  # Calculate the maximum length of the item names
  max_name_length = max(len(item1_name), len(item2_name))

  # Print the menu with the formatted prices and proper alignment
  print('/' + '-' * (max_name_length + 12) + '\\')
  print('| {:<{}s} {:>8}  |'.format(item1_name, max_name_length, formatted_price1))
  print('| {:<{}s} {:>8}  |'.format(item2_name, max_name_length, formatted_price2))
  print('\\' + '-' * (max_name_length + 12) + '/')

print_shop_menu('Apple', 3.99, 'Orange', 2.50)
print_shop_menu('Banana', 1.29, 'Grapefruit', 4.99)

