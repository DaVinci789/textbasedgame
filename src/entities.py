import argparse

import src.obj

worldEntities = []

player = src.obj.Player('nil', 100, 100, 10)

# Weapons:
weapons = [src.obj.Weapon('stick', 5, 'sword', 0, 'Whack to your heart\'s content.'),
           src.obj.Weapon('knife', 10, 'sword', 50, 'Ouch.'),
           src.obj.Weapon('gun', 50, 'projectile', 100, '3expensive5me'),
           src.obj.Weapon('cane', 6, 'sword', 5, 'The hidden power of old people everywhere'),
           src.obj.Weapon('fist', 3, 'melee', 0, 'Ah...the sweetness of stealing a body part from your enemies...'),
           src.obj.Weapon('sword', 40, 'sword', 80, 'Can slice even the most tough butter!')]


def getWeapon(name):
    for weapon in weapons:
        if weapon.name == name:
            return weapon
    print('Weapon ' + name + ' not found.')

# Special weapons that baddies don't have:
specialWeapons = [src.obj.Weapon('grenade', 10, 'bomb', 5, 'Throw it in your opponent\'s face!')]


def getSpecialWeapon(name):
    for specialWeapon in specialWeapons:
        if specialWeapon.name == name:
            return specialWeapon
    print('Weapon ' + name + ' not found.')

# Foods:
foods = [src.obj.Food('potato', 2, 2, 'Doesn\'t heal much, but it\'s nice and cheap.'), src.obj.Food('bread', 5, 5, 'Much more substantial food.'), src.obj.Food('health potion', 80, 60, 'Will heal you right up--but it comes with a price.')]


def getFood(name):
    for food in foods:
        if food.name == name:
            return food
    print('Food ' + name + ' not found.')

# Set up enemies
enemies = [src.obj.Enemy('assassin', 100, 10, "pet"), src.obj.Enemy('baby', 100, 1, "pet"), src.obj.Enemy('old lady', 100, 2, 'tickle')]


def getEnemy(name):
    for enemy in enemies:
        if enemy.name == name:
            return enemy
    print('Enemy ' + + ' not found.')

# Set up helpers
helpers = [src.obj.Helper('old lady'), src.obj.Helper('Gandalf'), src.obj.Helper('angel')]
helperItems = [getFood('potato'), getFood('bread'), getFood('health potion')]


def getHelper(name):
    for helper in helpers:
        if helper.name == name:
            return helper
    print('Helper ' + name + ' not found.')

# Set up memory characters
you = src.obj.Enemy('You', player.health, player.power, None)

# Vendors:
vendors = [src.obj.Vendor('food merchant', '\nHello! Welcome to my food store.', [getFood('bread'), getFood('potato')]), src.obj.Vendor('weapon trader', '\nI sell things to help you more efficiently kill people.', [getWeapon('gun'), getWeapon('knife'), getSpecialWeapon('grenade')])]


def getVendor(name):
    for vendor in vendors:
        if vendor.name == name:
            return vendor
    print('Vendor ' + name + ' not found.')

# Arguments:
argparser = argparse.ArgumentParser(description='A currently unnamed text-based game')
argparser.add_argument('-r', '--reset', help='Reset game', action='store_true')
argparser.add_argument('-l', '--load-game', help='Load existing game', action='store_true')
# argparser.add_argument('-s', '--use-language-espanol', help='Use Language other than English', action='store_true')
args = argparser.parse_args()

# Locations
locations = [src.obj.Location('Main', 'Where it all begins.', None), src.obj.Location('Inventory', 'Your Inventory.', None), src.obj.Location('Market', 'The Market.', None), src.obj.Location('Interact', 'Interact with your Surroundings.', None)]


def getLocation(name):
    for location in locations:
        if location.name == name:
            return location
    print('Location ' + name + ' not found')

# Help messages
helpMsgs = [src.obj.HelpMsg('Main', ['help--show this message', 'goto--goto <location>, ex. goto inventory', 'quit--quit game', 'reset--reset progress']), src.obj.HelpMsg('Inventory', ['help--show this message', 'list <food/money/weapons/health>--list wanted information', 'eat <food>--eat food and restore health', 'exit--leave inventory']), src.obj.HelpMsg('Market', ['help--show this message', '<item>--buy item', 'money--print available money', 'info <item>--give info on item', 'exit--leave the store'])]


def getHelpMsg(name):
    for helpMsg in helpMsgs:
        if helpMsg.name == name:
            return helpMsg
    print('Help Message ' + name + ' not found.')

# This file should not be executed
if __name__ == '__main__':
    print('Go away.')
