#Dylan Audley
#Adventure Functions
#09/24/2024


#Function that takes the price of an item, the amount of money you start with and how many you want to purchase and returns how many items you were able to purchase and the amount of money you have leftover.

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    num_purchased = ((startingMoney/itemPrice)-quantityToPurchase)
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

