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
#Comprueba Todas las opciones que tienes desde un habitacion y te las muestra
def listar(tipo):
  if tipo==1:
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
  elif tipo==2:
    if 'up' in rooms[currentRoom]:
      return 'up'
    if 'down' in rooms[currentRoom]:
      return 'down'
    if 'east' in rooms[currentRoom]:
      return 'east'
    if 'west' in rooms[currentRoom]:
      return 'west'
    if 'north' in rooms[currentRoom]:
      return 'north'
    if 'south' in rooms[currentRoom]:
      return 'south'
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
inventory = ['gun','amount']
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
                
            'Garden' : { 'north' : 'Dining Room',
                  'left' : 'Dining Room 2', #accés a la casa de convidats
            },
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
            'Bathroom' : { 'east'  : 'Despach',
              'south' : 'Living Room',
            },
            #Casa dels convidats
            #Planta principal 
            'Dining Room 2' : {'north': 'Kitchen 4',
              'west'  : 'Bathroom 2',
              'right' : 'Garden',
              'down'  : 'Gym 6'
            },
            'Kitchen 4' : {'up' : 'Room 1',
              'west' : 'Laundry 7',
              'south' : 'Dining Room 2',
            },
            'Laundry 7' : {'east' : 'Kitchen 4',
              'south' : 'Bathroom 2',
              'item' : 'lantern' #llinterna útil pel bunker
            },
            'Bathroom 2' : {'north' : 'Laundry 7',
              'east' : 'Dining Room 2',
            },
            'Gym 6' : {'up' : 'Dining Room 2',
              'right' : 'Bunker'
            },
            'Bunker' : {'left' : 'Gym 6'

            }

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
    listar(1)
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
      #Si fa mes de tres objectes hauria de treure algun
      if len(inventory)<3:
        #add the item to their inventory
        inventory += [move[1]]
        #display a helpful message
        print(move[1] + ' got!')
        #delete the item from the room
        del rooms[currentRoom]['item']
      else:
        print("-------------------------------------------------------")
        print("You have more objects.Which one do you want to release?")
        print("Inventory : " + str(inventory))
        item = input()
        if item in inventory:
          #add the item to their inventory
          inventory += [move[1]]
          #display a helpful message
          print(move[1] + ' got!')
          #delete the item from the room
          del rooms[currentRoom]['item']
          rooms[currentRoom]['item']=item
          for index,i_item in enumerate(inventory):
            if i_item==item:
              print("------------------------")
              print("You have lost the "+item)
              del inventory[index]
        else:
          print("----------------------------------")
          print("The object "+item+" does not exist")
          print('Can\'t get ' + move[1] + '!')
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      
      print('Can\'t get ' + move[1] + '!')
  # player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    # Si el jugador es troba al monter y te una gun y amount no mor
    if 'gun' in inventory and 'amount' in inventory:
      print("You found a monster but you have gun and munition")
      print("The shot gives him but doesn\'t kill him")
      #agafem una direccio posible
      direccion=listar(2)
      #anem a aquesta direccio
      currentRoom = rooms[currentRoom][direccion]
      #busquem el amount
      for index,amount in enumerate(inventory):
        if amount=='amount':
          print("You have lost the ammunition but you preserve the life")
          del inventory[index]
    else:
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
