import random
#!/bin/python3
def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Get to the Bunker and press the correct code to exit
With each successful attack the moster loses 2 hearts!
Commands:
  list(got all directions avaible) 
  go [direction]
  get [item]
''')
#Comprueba Todas las opciones que tienes desde un habitacion y te las muestra
def del_inventory_item(item):
  for index,i_item in enumerate(inventory):
    if i_item==item:
      print("------------------------")
      print("Lost "+item+"!")
      del inventory[index]
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
  print('---------- life of player','♥ '*l_player,'  ---------- life of monster: ','♥ '*l_monster)
  print('You are in the ' + currentRoom)
  #print the current inventory
  print("Inventory : " + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
def monster_random_room():
  previous_room=currentRoom
  rand=random.randrange(11)
  flag=True
  while flag:
    for index,key in enumerate(rooms.keys()):
      if index is rand:
        if currentRoom is key:
          rand=random.randint(index,11)
        else:
          new_room=key
          flag=False
          break
  if 'item 'in rooms[new_room]:
    rooms[previous_room]['item']=rooms[new_room]['item']
  else:
    del rooms[previous_room]['item']
  rooms[new_room]['item']='monster'
def monster_attack(life):
  rand=random.randrange(50)
  if rand%2 is 0:
    life=life-2
    return life
  else:
    return 'ok'
def person_random_room(room):
  rand=random.randrange(11)
  for index,key in enumerate(rooms.keys()):
    if index is rand:
      if room is key:
        rand=random.randint(index,11)
      else:
        currentRoom=key
        break
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
                  'item'  : 'Key(guest_house)'
                },
            'Workshop' : { 'north'  : 'Garage',
            },
            #Planta 0
            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'down'  : 'Garage',
                  'item'  : 'amount'
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
            'Bathroom' : { 'east'  : 'Despach',
              'south' : 'Living Room',
            },

         }
#Llave del sotano se usa
f_key_basement=False
#Llave de la casa de invitados
f_key_guest_house=False
#Definine iniatial life for player
l_player=4
#Definine iniatial life for monster
l_monster=3
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
  #eliminamos los espacios en blanco y lo convertimos en minuscula
  move = move.lower().strip()
  #dividimos por palabras
  move=move.split()
  #If move[0] = list - list the options avaiable
  if move[0] == 'list':
    listar(1)
  else:
    #comprovamos las palabras que hay si solo hay 1 faltan parametros
    if len(move)>1:
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
            print("----------------------")
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
          else:
            print("----------------------")
            print("You have more objects.")
            print("---------------------------------")
            print("Which one do you want to release?")
            print("Inventory : " + str(inventory) + " or Nothing")
            item = input('>')
            if item in inventory:
              #add the item to their inventory
              inventory += [move[1]]
              #display a helpful message
              print("----------------------")
              print(move[1] + ' got!')
              #delete the item from the room
              del rooms[currentRoom]['item']
              rooms[currentRoom]['item']=item
              del_inventory_item(item)
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
          print("---------------------------------------------------")
          print("You found a monster but you have gun and munition\n")
          print("The shot gives him but doesn\'t kill him")
          #agafem una direccio posible
          direccion=listar(2)
          #Movemos el mounstro antes de que se cambie la room
          monster_random_room()
          #anem a aquesta direccio
          currentRoom = rooms[currentRoom][direccion]
          #busquem el amount
          del_inventory_item('amount')
          #The monster lost one life
          l_monster=l_monster-1
      #Si tiene la pocion Puede elegir entr tirarla y huir o intentar escapat
        elif 'potion' in inventory:
          print("---------------------------------------------------")
          print('Choose one option:\n')
          print(' -Drink to Drink potion for restore one ♥ (Default)')
          print(' -Throw to Throw the potion and run. (50% of succes)')
          print("---------------------------------------------------")
          move = move
          opt=input('>')
          opt=opt.lower().strip().split()
          if opt[0] == 'throw':
            res=monster_attack(l_player)
            if res =='ok':
              print("You hit the bull's-eye and you manage to flee on time\n")
              print("Today you will not die")
            else:
              l_player=res
              print("You fail the launch and the monster manages to reach you\n")
              print("But fate smiles at you and you manage to escape")
          else:
            print("---------------------------------------------------")
            print('A monster has got you...\n You lost 2 ♥ of life')
            print("He attacks you but you take the potion and restore 1 ♥ of life")
            l_player=l_player-1
          person_random_room(currentRoom)
          monster_random_room()
          del_inventory_item('potion')
        else:
          l_player=l_player-2
          if l_player < 0 :
            print('A monster has got you... GAME OVER!')
            break
          else:
            print('A monster has got you...\n You lost 2 ♥ of life')
            print("---------------------------------------------------")
            person_random_room(currentRoom)
            monster_random_room()
      # player wins if they get to the garden with a key and a shield
      if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
      # player can go to the basement if got the key(basement)
      if f_key_basement is False:
        if currentRoom == 'Garage' and 'key(basement)' in inventory:
          print("-----------------------------")
          print("You have the key(basement)!!!\n")
          print("Use the key(basement) and open door.YOU ARE INSIDE!!!")
          del_inventory_item('key(basement)')
          f_key_basement=True
        elif currentRoom == 'Garage':
          print("You don't have the key(basement)!!!")
          currentRoom='Hall'
      if f_key_guest_house is False:
        if currentRoom == 'Dining room 2' and 'key(guest_house)' in inventory:
            print("-----------------------------")
            print("You have the key(guest_house)!!!\n")
            print("Use the key(guest_house) and open door.YOU ARE INSIDE SECOND HOUSE!!!")
            del_inventory_item('key(guest_house)')
            f_key_second_house=True
          elif currentRoom == 'Dining room 2':
            print("You don't have the key(guest_house)!!!")
            currentRoom='Garden'
      if currentRoom == 'Bunker':
        print("-----------------------------")
        print("You see a door with numeric keypad")
        print("Try the pin (5)\n")
        code = input('>')
        if code== '27426':
          print("You get to the bunker at last you're safe")
          print('YOU WIN!!!')
          break
        else:
          print('Check out all these rooms to see the code')
    else:
      print("------------------")
      print("Missing parameters")
