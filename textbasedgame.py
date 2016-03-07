#!/usr/bin/python3

# import inspect
import os

import src.obj
import src.utils
import src.locations
import src.languages
import src.entities


def commandLine():
    while True:
        try:
            command = input(': ').split(' ')
            if command[0] == '.':
                if src.entities.player.previousCommand is not None:
                    src.utils.execute(src.entities.player.previousCommand)
                else:
                    print('No previous command set')
            elif command[0].upper() == 'WHO':
                print('You are: ' + usr)
            elif command[0].upper() == 'QUIT':
                if src.utils.confirm('Are you sure you want to quit?'):
                    quitGame()
            elif command[0].upper() == 'RESET':
                if src.utils.confirm('Are you sure you want to reset?'):
                    newGame()
            else:
                src.utils.execute(command)
                src.entities.player.previousCommand = command
        except KeyboardInterrupt:
            quitGame()


def quitGame():
    print('\nSaving progress...')
    src.utils.saveInfo(usr, 'player.' + src.entities.player.name, src.entities.player)
    src.utils.saveInfo(usr, 'worldSrc.Entities', src.entities.worldSrc.Entities)
    try:
        src.utils.saveInfo(usr, 'previousVendor', previousVendor)
    except NameError:
        src.utils.saveInfo(usr, 'previousVendor', None)
    print('Progress saved.')
    exit(0)


def newGame():
    global usr
    usr = ''
    src.entities.worldSrc.Entities = []
    while not usr:
        try:
            usr = input('What is your desired username? : ')
        except KeyboardInterrupt:
            play()
    src.entities.player = obj.Player(usr, 100, 100, float(5))
    src.entities.player.inventory = [src.entities.getWeapon('stick'), src.entities.getFood('potato')]
    src.entities.player.location = src.entities.getLocation('Main')
    print('New Game set up. Welcome.')
    commandLine()


def loadGame():
    global usr, previousVendor
    try:
        users = []
        for file in os.listdir(src.utils.fileDir + '/saves'):
            if (file.endswith('.save') or file.endswith('.save.dat')):
                users.append(file.split('.')[0])
        try:
            usr = src.utils.choose('List of users:', users, 'What is your username?')
        except KeyboardInterrupt:
            play()
        src.entities.worldSrc.Entities = src.utils.loadInfo(usr, 'worldSrc.Entities')
        src.entities.player = src.utils.loadInfo(usr, 'player.' + usr)
        previousVendor = src.utils.loadInfo(usr, 'previousVendor')
        print('Game save loaded.')
        try:
            if src.entities.player.location == src.entities.getLocation('Inventory'):
                src.locations.inventory()
            elif src.entities.player.location == src.entities.getLocation('Market'):
                src.utils.goToVendor(previousVendor)
            elif src.entities.player.location == src.entities.getLocation('Interact'):
                src.utils.fight(src.entities.player.location.entity, src.entities.player.location.entity.weapon)
                # inventory()
        except KeyboardInterrupt or EOFError:
            quitGame()
        commandLine()
    except KeyError:
        print('Savefile does not exist or is broken. Creating new savefile...')
        newGame()


def play():
    while True:
        try:
            print('''
+----------------------------------------------+
| Welcome to textbasedgame!                    |
| This game is released under the GPL.         |
| Copyright V1Soft 2016                        |
+----------------------------------------------+''')
            choice = src.utils.choose('\nDo you want to:', [['Start a new game', 'new'], ['Continue from a previous save', 'continue'], ['Exit the game', 'quit']], '', False)
            if choice == 'NEW':
                newGame()
            elif choice == 'CONTINUE':
                loadGame()
            elif choice == 'QUIT':
                exit(0)
            else:
                while True:
                    if src.utils.confirm('Invalid option. Do you want to quit?'):
                        exit(0)
                    else:
                        break
        except KeyboardInterrupt or EOFError:
            exit(0)

if src.entities.args.reset:
    newGame()
elif src.entities.args.load_game:
    loadGame()
else:
    play()
