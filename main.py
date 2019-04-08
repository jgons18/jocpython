#!/bin/python3
def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Get to the Garden with a key and a potion
Avoid the monsters!
Commands:
  list(got all directions avaible) 
  go [direction]
  get [item]
''')
def listar():
  text=''
  if 'up' in rooms[currentRoom]:
    text+='   up    '
  if 'down' in rooms[currentRoom]:
    text+='   down  '
  if 'east' in rooms[currentRoom]:
    text+='   east  '
  if 'west' in rooms[currentRoom]:
    text+='   west    '
  if 'north' in rooms[currentRoom]:
    text+='   north   '
  if 'south' in rooms[currentRoom]:
    text+='   south   '
  print(text)
def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print("Inventory : " + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
#an inventory, which is initially empty
inventory = []
#a dictionary linking a room to other room positions
rooms = {
            #Planta -1
            'Garage' : { 'up'  : 'Hall',
                  'west' : 'Storage Room',
                  'south'    : 'Workshop',
                  'item'  : 'wrench'
              
                },
            'Storage Room' : { 'east'  : 'Garage',
                  'item'  : 'amount'
                },
            'Workshop' : { 'north'  : 'Garage',
            },
            #Planta 0
            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'down'  : 'Garage',
                  'item'  : 'key'
                },        
            'Kitchen' : { 'north' : 'Hall',
                  'item'  : 'monster'
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'up'    : 'Living Room',
                  'item'  : 'potion'
              
                },
                
            'Garden' : { 'north' : 'Dining Room' },
            #Planta 1
            'Living Room' : { 'east'  : 'Room',
                  'north' : 'Bathroom',
                  'down'    : 'Dining Room',
                  'item'  : 'gun'
              
                },
            'Room' : { 'west'  : 'Living Room',
              'north' : 'Despach',
              'item'  : 'key(basement)'
            },
            'Despach' : { 'west'  : 'Bathroom',
              'south' : 'Room',
              'item'  : 'amount'
            },

         }
#start the player in the Hall
currentRoom = 'Hall'
showInstructions()
#loop forever
while True:
  showStatus()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()
  #If move[0] = list list the options avaiable
  if move[0] == 'list':
    listar()
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')
  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  # player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
  # player wins if they get to the garden with a key and a shield
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house... YOU WIN!')
    break
  # player can go to the basement if got the key(basement)
  if currentRoom == 'Garage' and 'key(basement)' in inventory:
    print("You have the key!!!")
  elif currentRoom == 'Garage':
    print("You don't have the key!!!")
    currentRoom='Hall'
