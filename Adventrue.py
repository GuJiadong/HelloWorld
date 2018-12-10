# Austin Block, Jeffrey Gassenheimer, and Connor Hamilton
# CS021
# A text based adventure game where the user wakes up on an island, must find various objects, avoid death, and build a raft in order to escape
#coding=utf-8
import time
import sys


# main module worked on by all members
def main():
    # Variable that starts the game at main menu
    command = 'start'
    # Dictionary of commands that exist no matter what
    commandDict = {'left': 1, 'right': 1, 'forward': 1, 'search': 1, 'save': 1, 'bustedlogs': 0}
    # Dictionary of commands that user must find and refer to
    inventory = {'blessing': 0, 'knife': 0, 'firstLog': 0, 'secondLog': 0, 'thirdLog': 0, 'fourthLog': 0, 'rope': 0,
                 'sail': 0, 'rudder': 0, 'machete': 0, 'torch': 0, 'flint': 0, 'stick': 0, 'vines': 0, 'cannon': 0,
                 'helmet': 0}
    # checks for an existing save file and updates the inventory if found
    # Opening an existing save file written by Connor, Edited by Austin
    try:
        saveFile = open('save.txt', 'r')
        readFile = saveFile.readline().rstrip('\n')
        if readFile != '':
            while readFile != '':
                if readFile in inventory:
                    inventory[readFile] = 1
                readFile = saveFile.readline().rstrip('\n')
            if progressCheck(inventory):
                print("----------------------------------")
                print('Save loaded.')
                print("----------------------------------")
                print("Inventory found in File:")
                inventoryList(inventory)
                print("----------------------------------")
    except IOError:
        print('No existing save found.')
        print("----------------------------------")
    except ValueError:
        print('Corrupt save file, starting new game')
        print("----------------------------------")
    # add the inventory to the command dictionary
    commandDict.update(inventory)

    print("欢迎来到Adventure!")
    print("Main menu:")
    while command != 'exit' and command != 'begin':
        print("敲入 'begin' 来开始游戏\n敲入 'exit' 来退出游戏\n敲入 'commands'来查看游戏中的命令\n敲入 'new game' 来清除存档开始新的游戏\n")
        command = str(input('\033[1m' + "Enter command: " + '\033[0m'))
        if command != 'exit':
            if command == 'commands':
                commandMenu()
            elif command == 'new game':
                newGame()
            elif command == 'begin':
                print("----------------------------------")
                # checks the inventory to see if any progress has been made to give the correct opening line
                if progressCheck(inventory):
                    print('You are at the beach. Choose an action to take.')
                else:
                    print('你醒来时听到海浪拍打着岩石的声音.\n尽可能多地吐出你嘴里的沙子,你的眼睛慢慢适应明亮的正午阳光,你蹒跚地走着,然后悄悄地试着弄清周围的环境.\n你不记得你是怎么来到这里的,或者你来自哪里,但现在有两件事情很清楚.\n你在一个孤立的的岛屿上,你没有办法离开. \n现在,选择行走方向或搜索周边地区.')
                print('\033[1m' + '如果您安全返回此处,则只能保存进度.' + '\033[0m')
                beach(commandDict)
        # function to exit game added by Connor
        if command == 'exit':
            print('Game Exited')
            sys.exit()


# Function to print inventory commands by Austin and Jeffrey
def commandMenu():
    print('\033[1m' + '下面的命令是随时可用的:')
    print('\033[0m' + 'LEFT: 角色将会向左行进')
    print('RIGHT: 角色将会向右行进')
    print('FORWARD: 角色将会向前行进')
    print('SAVE: 只有当你在海滩的时候才可以使用,将会在退出游戏时保存你的进度.')
    print('SEARCH: 对你周围进行搜索将看到的物品捡入背包.')
    print('\033[1m' + '以下命令要求在使用前拾取对象:')
    print('\033[0m' + 'KNIFE: 角色将使用小刀')
    print('BLESSING: you cheeky little bugger')
    print('MACHETE: 角色将使用弯刀')
    print('TORCH: 角色将点燃火炬')
    print('FLINT: 角色将使用燃石')
    print('CANNON: 角色将点燃大炮进行射击')
    print('RAFT: 角色将逃离小岛')
    print('\033[1m' + '有些物品未被归入命令,你得找到他们.' + '\033[0m')
    input("按enter键返回菜单: ")
    print("----------------------------------")


def commandMenuInGame():
    print('\033[1m' + '下面的命令是随时可用的:')
    print('\033[0m' + 'LEFT: 角色将会向左行进')
    print('RIGHT: 角色将会向右行进')
    print('FORWARD: 角色将会向前行进')
    print('SAVE: 只有当你在海滩的时候才可以使用,将会在退出游戏时保存你的进度.')
    print('SEARCH: 对你周围进行搜索将看到的物品捡入背包.')
    print('\033[1m' + '以下命令要求在使用前拾取对象:')
    print('\033[0m' + 'KNIFE: 角色将使用小刀')
    print('BLESSING: you cheeky little bugger')
    print('MACHETE: 角色将使用弯刀')
    print('TORCH: 角色将点燃火炬')
    print('FLINT: 角色将使用燃石')
    print('CANNON: 角色将点燃大炮进行射击')
    print('\033[1m' + '有些物品未被归入命令,你得找到他们.' + '\033[0m')
    print("----------------------------------")

# Function to save progress by Connor
def saveGame(commandDict):
    saveFile = open('save.txt', 'w')
    inventory = inventoryOnly(commandDict)
    for n in inventory:
        for i in range(0, inventory[n], 1):
            saveFile.write(n + '\n')
    saveFile.close()
    print('Game saved')
    return


# function to check progress of save file by Connor
# used so that if there is a save with no progress, it is treated as if it was a new game
def progressCheck(inventory):
    progress = True
    totalItems = 0
    for n in inventory:
        totalItems += inventory[n]
    if totalItems == 0:
        progress = False
    return progress


# function to wipe an existing save file by Connor
def newGame():
    try:
        saveFile = open('save.txt', 'w')
        saveFile.close()
        print('现有的保存已被删除.')
    except IOError:
        print('尝试打开文件时发生错误.')
    except:
        print('发生错误.')
    main()


# ERROR CHECKING WRITTEN BY JEFFREY AND AUSTIN
# Function to get user input, make sure a string, make sure valid command
def errorChecking(commandDict):
    while True:
        inString = input('\033[1m' + "Enter command: " + '\033[0m')
        if isinstance(inString, str):
            inString = inString.lower()
            # Call command list if requested (added by Connor)
            if inString == 'commands':
                commandMenuInGame()
            # Return to menu if requested (added by Connor)
            elif inString == 'menu':
                main()
            # List inventory (added by Connor)
            elif inString == 'inventory':
                inventoryList(commandDict)
            # Check for valid commands
            elif inString in commandDict:
                # Get value for the key
                currentValue = commandDict[inString]
                if currentValue >= 1:
                    return inString
                else:
                    print("You entered something that is not in your possession or abilities. Please try again.")
            else:
                print("You entered something that was not a valid command. Please try again.")
        else:
            print("You entered something that was not a string. Please try again.")


# function to list out current inventory items by Connor
def inventoryList(commandDict):
    inventory = inventoryOnly(commandDict)
    for n in inventory:
        if n != 'firstLog' and n != 'secondLog' and n != 'thirdLog' and n != 'fourthLog':
            if inventory[n] > 0:
                print(n, 'x' + str(inventory[n]))
    if countLogs(inventory) > 0:
        print('logs x' + str(countLogs(inventory)))


# function to separate commands out of commandDict to reference only inventory items by Connor
def inventoryOnly(commandDict):
    commandList = ('left', 'right', 'forward', 'search', 'save', 'bustedlogs')
    inventory = {}
    for n in commandDict:
        if n not in commandList:
            inventory[n] = commandDict[n]
    return inventory


# function to count unique logs so they don't clutter inventory by Connor
def countLogs(commandDict):
    total = commandDict['firstLog'] + commandDict['secondLog'] + commandDict['thirdLog'] + commandDict['fourthLog']
    return total


# BEACH Written by All

def beach(commandDict):
    activeCommand = errorChecking(commandDict)
    while (activeCommand != 'left' and activeCommand != 'right' and activeCommand != 'forward' and activeCommand != 'raft' and activeCommand != 'helmet'):
        # If user searches they find a knife
        if (activeCommand == 'search'):
            currentValue = commandDict['knife']
            if currentValue == 0:
                print("You searched and found a knife in the sand.")
                commandDict['knife'] = 1
            # If knife was already taken, nothing is found
            elif currentValue == 1:
                print("You searched and found nothing.")
        # If user saves, the current inventory is saved
        elif activeCommand == 'save':
            saveGame(commandDict)
        # If user attempts to do anything else, nothing happens
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # Left takes user to shipwreck
    if activeCommand == 'left':
        print("You stumble across the rocky beach to the partially intact remains of a wooden sailing ship.")
        shipwreck(commandDict)
    # Forward takes user to forest
    elif activeCommand == 'forward':
        print("You come to stand at the entrance of a forest with trees on all sides.")
        forest(commandDict)
    # Right takes user to cave
    elif activeCommand == 'right':
        cave(commandDict)
    # Helmet takes user to shrine
    elif activeCommand == 'helmet':
        shrine(commandDict)
    # endgame by Connor
    elif activeCommand == 'raft':
        # If all items have been found...
        if commandDict['rudder'] == 1 and commandDict['firstLog'] == 1 and commandDict['secondLog'] == 1 and \
                commandDict['thirdLog'] == 1 and commandDict['fourthLog'] == 1 and commandDict['sail'] == 1:
            # ...Raft is built
            print('You have all the materials to make a raft! You get to work and are finished in no time.')
            # If blessing was found, user survives and successfully completes game
            if commandDict['blessing'] == 1:
                print('Against all odds, you have made it safely back to land. Something was looking out for you...')
            # If no blessing, user dies
            else:
                print('You set sail and immediately after getting into deeper water, you see something swimming under you.')
                print('Suddenly, a monster from the depths rises out of the water and eats you for breakfast.')
                print("You will spend the rest of your time slowly being digested in the monster's stomach.")
                print('Seems like you may have not have been blessed to escape from that island yet.')
                return


# Code for Shipwreck and Pirate ship written exclusively by Connor

# Shipwreck by Connor


# function to start the shipwreck area
def shipwreck(commandDict):
    print("You stand in front of the ship, looking up at it. It is much larger than it appeared from the beach.")
    print("There is a small hole in the front of the ship and you can partially make out the rotting interior")
    activeCommand = errorChecking(commandDict)
    while activeCommand != 'left' and activeCommand != 'right' and activeCommand != 'forward':
        if activeCommand == 'search':
            if commandDict['flint'] == 1:
                print('You search around the outside of the ship and find nothing.')
            else:
                if commandDict['stick'] == 0:
                    print('You search around the outside of the ship and find a small piece of flint.')
                    print('Good for hitting on rocks and making bright flashes. You wonder if it has any real use...')
                    commandDict['flint'] = 1
                else:
                    print(
                        'You search around the outside of the ship and find a small piece of flint. You can use it to light the torch.')
                    commandDict['stick'] = 0
                    commandDict['torch'] = 1
                    commandDict['flint'] = 1
            activeCommand = errorChecking(commandDict)

        else:
            print('That will not work right now.')
            activeCommand = errorChecking(commandDict)

    if activeCommand == 'right':
        print('You travel to the forest.')
        forest(commandDict)
    elif activeCommand == 'forward':
        print('You squeeze through the small hole in the hull and find yourself in the dimly lit main hallway.')
        print('You travel through the hallway, which is slanted upwards from the angle of the wrecked ship.')
        print()
        shipInMainHall(commandDict)
    elif activeCommand == 'left':
        print('You travel to the beach')
        beach(commandDict)


# function to describe the main interior of the ship
def shipInMainHall(commandDict):
    print('You are standing in a room inside the shipwreck, looking at the rotten and broken interior.')
    print('The floor has fallen out on the other side of the room, and on the far side, you can see an opening to the rest of the ship.')
    print('There is an opening to your left and you can see a path down to where you were standing in front of the ship.')
    print('There is a door to your right.')
    activeCommand = errorChecking(commandDict)
    # loop to keep commands coming if player stays in this area
    while activeCommand != 'left' and activeCommand != 'forward':
        # find the third log
        if activeCommand == 'search':
            if commandDict['thirdLog'] == 0:
                print("You see an intact log, but it is wrapped in rotten rope and you can't get it free.")
            else:
                print('You have already found the log here. You need 4 to make the raft.')
            activeCommand = errorChecking(commandDict)
        elif activeCommand == 'knife':
            if commandDict['thirdLog'] == 0:
                print('You cut the log free using the knife.')
                commandDict['thirdLog'] = 1
            else:
                print('You have already found the log here. You need 4 to make the raft.')
            activeCommand = errorChecking(commandDict)
        # fake direction. acts as if you are traveling, but only the text actually moves, not the code
        elif activeCommand == 'right':
            # check for inventory items to give correct response
            if commandDict['flint'] == 0 and commandDict['stick'] == 0:
                print(
                    'You open the door and find a dry torch. But until you have something to light it with, it is a stick and that is what we are calling it.')
                commandDict['stick'] = 1
            elif commandDict['flint'] == 1 and commandDict['torch'] == 0:
                print('You open the door and find a dry torch. You can use the flint you found before to light it.')
                commandDict['torch'] = 1
            else:
                print('You open the door and find nothing of interest.')
            activeCommand = errorChecking(commandDict)
        else:
            print("That won't work right now.")
            activeCommand = errorChecking(commandDict)
    if activeCommand == 'forward':
        if commandDict['vines'] == 1:
            print('You use the vines you found in the forest to safely get across the gap to the other side.')
            print('Pulling the vines down and putting it back in your inventory, you turn around and look at the opening.')
            print('It looks like this is an entire new section of the ship. But nothing seems to be rotten. Actually it is in very good condition... Wait...')
            time.sleep(12)
            print()
            print('It is an entirely different ship! They must have come up and docked their ship next to the wreck while you were wasting time messing around.')
            print('You cautiously walk forwards and make your way on to the ship, because we know you are good at making smart decisions.')
            print('As you make your way, you can see what must be the crew walking down the beach to a side of the island you have not been to. Lucky you.')
            print('You notice that the flag the ship sails is black and has a human skull crossed with a fork and knife.')
            print('Unfortunately you still have not regained your memory so this means nothing to you.')
            pirateShip(commandDict)
        else:
            print('You walk forwards and plummet to your death. I mean really, what did you think would happen?')
            print("Next time don't try to free climb without something to hold you.")
            return
    else:
        print('You go out the left side of the ship and make your way down to where you were standing in front of it.')
        print('The way down was not easy, and you had to jump the last part. You will not be able to come back up this way.')
        shipwreck(commandDict)


# function to start the pirate ship section of the adventure by Connor
def pirateShip(commandDict):
    print()
    print('You are now on the deck of the ship. There is a line of cannons on either side of you. Whoever these guys are, they mean business.')
    print('To you right is the front of the ship, looking at the island.')
    print('To your left is the back of the ship, with a door that leads further into the ship.')
    print('What do you want to do?')
    activeCommand = errorChecking(commandDict)
    while activeCommand != 'right' and activeCommand != 'left':
        if activeCommand == 'search':
            print(
                "You look around but all you see of interest are the cannons, and they're all tied down so don't get any ideas.")
            activeCommand = errorChecking(commandDict)
        elif activeCommand == 'knife' and commandDict['knife'] == 1 or activeCommand == 'machete' and commandDict[
            'machete'] == 1:
            print('Alright fine, be that way. You can have the cannon.')
            commandDict['cannon'] = 1
            activeCommand = errorChecking(commandDict)
        else:
            print("You can't do that right now.")
            activeCommand = errorChecking(commandDict)
    if activeCommand == 'right':
        print('You go back to the place you were standing in front of the shipwreck.')
        shipwreck(commandDict)
    elif activeCommand == 'left':
        print('You go down through the door, because as we have established, you make good decisions.')
        print('You are standing at the end of a hallway.')
        print('To your right and front there are two doors.')
        print('The way back up is to your left.')
        activeCommand = errorChecking(commandDict)
        while activeCommand != 'left':
            if activeCommand == 'search':
                print('You look around and find nothing.')
            elif activeCommand == 'right':
                print('You go through the door and find a band of crew members drinking and playing safe games involving swords and guns. How did you not hear them?')
                time.sleep(4)
                print()
                print('They turn around at the sound of your grand entrance and decide to incorporate you into their next round of games.')
                print('Unfortunately, you are not on the participating end of the games. Better luck next time.')
                return
            elif activeCommand == 'forward':
                print('You go into a small closet and see a spare rudder. This could be handy.')
                print('You put the rudder in your inventory and go back out to the hallway.')
                commandDict['rudder'] = 1
                activeCommand = errorChecking(commandDict)
            else:
                print('That will not work right now.')
                activeCommand = errorChecking(commandDict)

        if activeCommand == 'left':
            print('You make your way back up to the deck of the ship.')
            pirateShip(commandDict)


# Code for Forest and Swamp written exclusively by Austin

# FOREST WRITTEN BY AUSTIN
def forest(commandDict):
    # Determine surroundings based on if cannon previously blew up trees in the way
    # If logs are busted, inform user that they can travel anywhere
    if commandDict['bustedlogs'] == 1:
        print("You can go any direction, routes are clear to the left, right, and forward.")
        print("A far distance behind you is the beach however you consider the amazing things that might be hidden")
        print("in this forest.")
    # If logs exist, inform user that logs are in the way
    else:
        print("There are a couple of fallen trees in front of you and the route is impassible.")
        print("There is a route to both the right and left however.")
        print("A far distance behind you is the beach however you consider the amazing things that might be hidden")
        print("in this forest.")
    # Get action from user
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right
    while (activeCommand != 'left' and activeCommand != 'right'):
        if (activeCommand != 'forward' and activeCommand != 'cannon'):
            # Search command results in nothing
            if (activeCommand == 'search'):
                print("You found nothing but dirt.")
            # All other commands do not work
            else:
                print("That command will not work right now.")
        # Use cannon
        elif activeCommand == 'cannon':
            # Cannon should bust the logs and inform user that route is cleared
            if commandDict['bustedlogs'] == 0:
                print(
                    "You have used the cannon to blow up trees blocking your path forward. It might be worth checking out what")
                print("lies deeper in the forest. Some sunlight up ahead indicates a possible clearing.")
                commandDict['bustedlogs'] = 1
            # If cannon was already used here, do not do anything but inform user
            elif commandDict['bustedlogs'] == 1:
                print("You have already blown up the trees here and the cannon will do you no good.")
        # Go forward
        elif activeCommand == 'forward':
            # Forward occurs, taking you to swamp, if logs are busted
            if commandDict['bustedlogs'] == 1:
                print("You have traveled forward, through where trees used to block the path...")
                time.sleep(1)
                print("It is beginning to get a bit muddy but you continue forward.")
                time.sleep(1)
                swamp(commandDict)
                return
            # If logs are not busted, nothing happens but inform user
            elif commandDict['bustedlogs'] == 0:
                print("There are still a couple of fallen trees in front of you and the route is still impassible.")
                print("You cannot go forward until you have cleared the route.")
        activeCommand = errorChecking(commandDict)
    # For command LEFT go to FOREST LEFT
    if activeCommand == 'left':
        print("You have gone a few steps to the left, there appears to be an route between some trees here.")
        forestLeft(commandDict)
    # For command RIGHT go to FOREST RIGHT
    elif activeCommand == 'right':
        print(
            "You have gone a few steps to the right, there appears to be a cave some distance from you.\nIt also looks as if someone had previously set up camp here.")
        forestRight(commandDict)


# FOREST LEFT WRITTEN BY AUSTIN
def forestLeft(commandDict):
    # Get action from user
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right or forward
    while (activeCommand != 'left' and activeCommand != 'right' and activeCommand != 'forward'):
        # If search you find a log
        if (activeCommand == 'search'):
            # Get log if needed
            if commandDict['firstLog'] == 0:
                print("You found a log and added it to your possessions.")
                commandDict['firstLog'] = 1
            # Ignore log if you already have this one
            else:
                print("You already found the log that was here earlier.")
                print("Maybe there are a few others elsewhere though, four are necessary to build the raft.")
        # If machete, you hit foot and die
        elif (activeCommand == 'machete'):
            currentValue = commandDict['machete']
            print("You used the machete and accidentally hit your foot. Blood is spraying everywhere...")
            time.sleep(2)
            print("You died")
            return
        # For anything else you have but can't use
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # For command FORWARD
    if activeCommand == 'forward':
        deepForestLeft(commandDict)
    # For command LEFT
    if activeCommand == 'left':
        print('You have come across a shipwreck!')
        shipwreck(commandDict)
    # For command RIGHT
    elif activeCommand == 'right':
        deepForestLeft(commandDict)


# FOREST RIGHT WRITTEN BY AUSTIN
def forestRight(commandDict):
    # In forest right you can search to find a machete, go straight to end up in a cave, go left to nothing, or right to beach, find logs
    # Get action from user
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right or forward
    while (activeCommand != 'right' and activeCommand != 'forward'):
        # If search you find a log
        if (activeCommand == 'search'):
            # Get log if needed
            if commandDict['secondLog'] == 0:
                print("You found a log by the campsite and added it to your possessions.")
                commandDict['secondLog'] = 1
            # Ignore log if you already have four
            else:
                print("You already found the log that was here earlier.")
                print("Maybe there are a few others elsewhere though, four are necessary to build the raft.")
            # Get machete if needed
            if commandDict['machete'] < 1:
                print("You also found a machete by the campsite and added it to your possessions.")
                commandDict['machete'] = 1
            # Ignore log if you already have four
            else:
                print("You found a machete but already have one.")
        elif (activeCommand == 'left'):
            print("There is bramble on your left so you can't go that direction.")
        # For anything else you have but can't use
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # For command FORWARD go to cave
    if activeCommand == 'forward':
        print("You are heading towards the cave you saw earlier...")
        time.sleep(1)
        cave(commandDict)
    # For command RIGHT go to beach
    elif activeCommand == 'right':
        print("You are back on the beach now. Have you found enough stuff to build the raft yet?")
        beach(commandDict)


# DEEP FOREST LEFT WRITTEN BY AUSTIN
def deepForestLeft(commandDict):
    # Description of deep forest left
    print("You are surrounded by trees now. In the distance you see vines hanging.")
    print("Ponder what vines might do to help you out.")
    # Get action from user
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right or forward
    while (activeCommand != 'left' and activeCommand != 'right' and activeCommand != 'forward'):
        # If torch it is wasted
        if (activeCommand == 'torch'):
            commandDict['torch'] = 0
            print("You just wasted your torch, better go find another.")
        # For anything else you have but can't use
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # For command FORWARD
    if activeCommand == 'forward':
        deepForestLeftForward(commandDict)
    # For command LEFT
    if activeCommand == 'left':
        print('You make your way over to the shipwreck.')
        shipwreck(commandDict)
    # For command RIGHT
    elif activeCommand == 'right':
        print("You have gone a few steps to the right and are close to where you entered the forest.")
        forestLeft(commandDict)


# EXTENSION OF DEEP FOREST LEFT WRITTEN BY AUSTIN
def deepForestLeftForward(commandDict):
    print("You have gone even deeper into the forest. There is a shipwreck to your left now.")
    # Get action from user
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right or forward
    while (activeCommand != 'left' and activeCommand != 'right'):
        # If machete you get rope
        if (activeCommand == 'machete'):
            commandDict['vines'] = 1
            print("You cut down vines and it added it to your possessions.")
            print("Vines will come in handy for assembling the raft as no nails are available.")
        # If forward you run into a bush
        elif (activeCommand == 'forward'):
            print("There are vines in front of you, you cannot go that direction.")
        # For anything else you have but can't use
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # For command LEFT go to shipwreck
    if activeCommand == 'left':
        print('You make your way over to the wreck of the sailing ship.')
        time.sleep(1)
        shipwreck(commandDict)
    # For command RIGHT go back to forest left
    elif activeCommand == 'right':
        print("You have gone a few steps to the right and are close to where you entered the forest.")
        forestLeft(commandDict)


# THE FIRST LEVEL OF SWAMP
def swamp(commandDict):
    print(
        "There are some strange looking things off to the right. The area in front of you appears to be quicksand followed by a swamp.")
    print(
        "You ponder if you should attempt going through the quicksand. The swamp after it looks interesting--but is it worth the risk?")
    # Get action from user
    activeCommand = errorChecking(commandDict)
    while (activeCommand != 'left' and activeCommand != 'right' and activeCommand != 'forward'):
        # If search you find nothing
        if (activeCommand == 'search'):
            print("You found nothing but dirt.")
        # For anything else you have but can't use
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # For command FORWARD go to QUICKSAND
    if activeCommand == 'forward':
        # Print some warning messages without allowing further action
        print("Uh oh. You are standing in quicksand.")
        time.sleep(1)
        print("Better think fast!")
        time.sleep(1)
        print("Too late. You died.")
        # Death ends program by returning
        return
    # For command LEFT
    elif activeCommand == 'left':
        print('You are walking back to the forest entrance on your previous trail...')
        time.sleep(1)
        # Another subtle hint if user did not search and find both objects
        if (commandDict['sail'] == 0 and commandDict['helmet'] == 0):
            print('You begin to wonder if you had indeed seen something else behind you...')
            time.sleep(1)
        forest(commandDict)
    # For command RIGHT
    elif activeCommand == 'right':
        swampRight(commandDict)


# SWAMP RIGHT
def swampRight(commandDict):
    # Print welcome to the swamp right and inform user of their surroundings
    print("Wow, there is a pile of leftover belongings here. Might be worth checking them out.")
    print("Someone else must have also been stuck on this island. Unfortunately, most of the stuff is rusted;")
    print("however, some of it is not!")
    # Get action from user
    activeCommand = errorChecking(commandDict)
    while (activeCommand != 'left' and activeCommand != 'right'):
        # Forward run into pile of leftover belongings
        if activeCommand == 'forward':
            print("There is a pile of leftover belongings in front of you. You cannot go forward.")
        # Have neither helmet or sail
        elif activeCommand == 'search' and commandDict['helmet'] == 0 and commandDict['sail'] == 0:
            commandDict['helmet'] = 1
            print(
                "You found an old helmet and put it on. You wonder why someone would have had this--but it does not matter.")
            print("There is still a pile of more leftover belongings.")
        # Have helmet but no sail
        elif activeCommand == 'search' and commandDict['helmet'] == 1 and commandDict['sail'] == 0:
            commandDict['sail'] = 1
            print("You found a sail and added it to your possessions.")
        # Somehow have sail but no helmet
        elif activeCommand == 'search' and commandDict['helmet'] == 0 and commandDict['sail'] == 1:
            print(
                "You found an old helmet and put it on. You wonder why someone would have had this--but it does not matter.")
        # Have both items, search results in nothing
        elif activeCommand == 'search' and commandDict['helmet'] == 1 and commandDict['sail'] == 1:
            print("You searched and found nothing else that is helpful.")
        # Else does nothing
        else:
            print("That command will not work right now.")
        # Let user enter another command
        activeCommand = errorChecking(commandDict)
    # Left go back to swamp
    if activeCommand == 'left':
        swamp(commandDict)
    # Right go back to forest
    elif activeCommand == 'right':
        print('You are walking back to the forest entrance on a separate trail...')
        time.sleep(1)
        # If user missed an object, which is found upon the search command, give them subtle hint
        if (commandDict['sail'] == 0 and commandDict['helmet'] == 0):
            print('You begin to wonder if you had indeed seen something else back by the swamp...')
            time.sleep(1)
        forest(commandDict)


# Code for Cave and Shrine Written Exclusively by Jeffrey

# Cave Written by Jeffrey
def cave(commandDict):
    print("You happen upon a cave, a crevice torn out of the side of a hill, descending deep into the earth.\n"
          "its interior is pitch black, and barely any sunlight penetrates the shadows.\n"
          " the forest is to your left and the beach to your right.")
    # Get action from user
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right
    while (activeCommand != 'left' and activeCommand != 'right'):
        if (activeCommand == 'search' and commandDict['torch'] == 0):
            print("You head into the dark cave with absolutely nothing to light your way.\n"
                  "In the darkness a snake lashes out and bite your foot.\n"
                  "You have died.")
            return
        elif (activeCommand == 'search' and commandDict['torch'] == 1):
            print(
                "Hunting around in the cave illuminated by your torch, you stumble across a skeleton, there is a machete clutched in its grip. \n"
                "You pry it free. It has been added to your possessions.")
            commandDict['machete'] = 1
        # If machete you get rope
        elif (activeCommand == 'machete' and commandDict['torch'] == 1):
            commandDict['rope'] += 1
            print("You cut down vines to use as rope, it has been added to your possessions.")
        elif (activeCommand == 'knife' and commandDict['torch'] == 1):
            commandDict['rope'] += 1
            print("You cut down vines to use as rope, it has been added to your possessions.")
        # For anything else you have but can't use
        elif (activeCommand == "torch"):
            print("You drop you torch and it strikes a distinct shape! You've found another log!")
            commandDict['fourthLog'] = 1
        elif (activeCommand == 'cannon'):
            print(
                "You fired off a cannon inside an enclosed cave, setting off a cave in, crushing you under a ton of stone.\n"
                "You have died.")
            return
        else:
            print("That command will not work right now.")
        activeCommand = errorChecking(commandDict)
    # For command LEFT
    if activeCommand == 'left':
        print("You head along to the left and arrive at the forest.")
        forest(commandDict)
    # For command RIGHT
    elif activeCommand == 'right':
        print("You head right and wind up at the beach to beach.")
        beach(commandDict)


# shrine location by jeffrey
def shrine(commandDict):
    print(
        "You decend through the depths, seeing a faith glowing structure hidden where the island meets the seafloor, it appears as some kind of ancient shrine.")
    # Get action from user
    timer = 0
    activeCommand = errorChecking(commandDict)
    # For commands OTHER than left or right or forward
    while (activeCommand != 'forward'):
        if (timer == 3):
            print("Water rushes into your cracked diving bell. you have died.")
            return
        elif (activeCommand == 'search'):
            print("You scrabble around the shrine, exposing some characters previously covered in dust.")
            print("L-GH- --E BL-S- TO -H-W R--P-CT")
            timer += 1
        elif (activeCommand == "torch"):
            print("You just tried to use a torch UNDERWATER. How can you possibly be this dumb.")
            commandDict["torch"] = 0
            timer += 1
        elif (activeCommand == 'cannon'):
            print("With a THUNDERING ROAR, the blast wave from the cannon ripples out in the water.\n"
                  "Surprisingly you are not crushed by the intense pressure but rather feel a warm glow within your body, you'd best return to the surface.")
            commandDict["blessing"] = 1
        else:
            print("That command will not work right now.")
            timer += 1
        if (timer == 1):
            print("Water presses against the outside of your diving bell. \n"
                  "Not much time remains, you'd best hurry.")
        elif (timer == 2):
            print("Cracks begin to appear along the glass, you have barely any time left.")
        activeCommand = errorChecking(commandDict)
    # For command forward
    if activeCommand == 'forward':
        print("You return to the surface.")
        beach(commandDict)

main()