import os
from inventory import inventory
from instruction import Instruction

def status():
    print("----------")
    print(f"Current Room: {currentRoom}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        room_item = rooms[currentRoom]["item"]
        print(f"You see a {room_item}")
    else:
        print(f"You don't see anything")
    print("----------")

currentRoom = "Entrance"

Instruction()

rooms = {
    "Outside" : {
        "north": "Entrance"
    },
    "Entrance"  : {
        "north": "Lobby",
        "south": "Outside"
    },
    "Lobby": {
        "south": "Entrance",
        "east" : "Vestibule",
        "west" : "Downstairs Bathroom",
        "north" : "Living Room"
    },
    "Living Room": {
        "south" : "Lobby",
        "east" : "Walkin Closet",
        "west" : "Kitchen",
        "north" : "Staircase F1",
        "item" : "robe"
    },
    "Vestibule" : {
        "west" : "Lobby",
        "east" : "Garage",
    },
    "Garage" : {
        "west" : "Vestibule",
        "item" : "steel pipe"
    },
    "Downstairs Bathroom" : {
        "east" : "Lobby",
        "item" : "areosol can"
    },
    "Walkin Closet" : {
        "west" : "Living Room",
        "item" : "lighter"
    },
    "Kitchen" : {
        "east" : "Living Room",
        "north" : "Backyard",
        "item" : "knife"
    },
    "Backyard" : {
        "south" : "Kitchen",
    },
    "Staircase F1" : {
        "south" : "Living Room",
        "up" : "Staircase F2",
    },
    "Staircase F2" : {
        "south" : "Landing",
        "down" : "Staircase F1",
    },
    "Landing" : {
        "north" : "Staircase F2",
        "west" : "Storage",
        "east" : "Guest Bedroom",
        "south" : "Hallway",
    },
    "Hallway" : {
        "north" : "Landing",
        "west" : "Upstairs Bathoom",
        "east" : "Master Bedroom",
    },
    "Guest Bedroom" : {
        "west" : "Landing",
        "item" : "steel pipe"
    },
    "Storage" : {
        "east" : "Landing",
        "item" : "pistol"
    },
    "Upstairs Bathoom" : {
        "east" : "Hallway",
    },
    "Master Bedroom" : {
        "west" : "Hallway",
        "up" : "Attic",
    },
    "Attic" : {
        "down" : "Master Bedroom",
        "item" : "demon"
    }
}   

print("I am in the", currentRoom)


while True:

    status()

    move = input(">")
    move = move.split(" ", 1)

    os.system("clear")

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            print(f"You are now in the {currentRoom}")
        else:
            print(f"You can't go {move[1]}")
        

    if move[0] == "get":
        if move[1] == rooms[currentRoom]["item"]:
            print(f"You picked up a {move[1]}")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = ""
            print(inventory)
        else:
            print(f"You don't see a {move[1]}")
    
    # Victory 1
    if "robe" in inventory and "knife" in inventory and currentRoom == "Attic":
        print("You disguised yourself as the demon's summoner and caught it off guard")
        print("You killed the demon you return home mission complete")
        break
    
    # Victory 2
    if "areosol can" in inventory and "lighter" in inventory and "steel pipe" in inventory and currentRoom == "Attic":
        print("The demon saw you and attacked you make a makeshift flamethrower to damage the demon")
        print("With all your strength you managed to kill the demon with a steel pipe")
        print("You return home mission complete")
        break

    # Victory 3
    if "pistol" in inventory and currentRoom == "Attic":
        print("You see the demon before it has a chance to react you unload every bullet into it")
        print("As it's body lie dead you realize your mission is complete you return home")
        break
    
    # Loss 1
    if currentRoom == "Outside":
        print("Try as you might you couldn't work up the nerve to enter the house")
        print("Guess you were never cut out to be a devil buster")
        print("GAME OVER")
        break
    
    # Loss 2
    if currentRoom == "Attic":
        print("The demon saw you and attacked you weren't able to fight back with what you had")
        print("You suffered the fate many unqualified devil busters before you")
        print("GAME OVER")
    
