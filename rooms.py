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
    "Entrance"  : {
        "north": "Lobby",
        "item" : "steel pipe"
    },
    "Lobby": {
        "south": "Entrance",
        "west" : "Vestibule",
        "east" : "Downstairs Bathroom",
        "north" : "Living Room"
    },
    "Living Room": {
        "south" : "Lobby",
        "east" : "Walkin Closet",
        "west" : "Kitchen",
        "north" : "Staircase F1",
    },
    "Vestibule" : {
        "east" : "Lobby",
        "west" : "Garage",
    },
    "Garage" : {
        "east" : "Vestibule",
    },
    "Downstairs Bathroom" : {
        "west" : "Lobby",
    },
    "Walkin Closet" : {
        "west" : "Living Room",
    },
    "Kitchen" : {
        "east" : "Living Room",
        "north" : "Backyard",
    },
    "Backyard" : {
        "south" : "Kitchen",
    },
    "Staircase F1" : {
        "north" : "Living Room",
        "up" : "Staircase F2",
    },
    "Staircase F2" : {
        "south" : "Landing",
        "down" : "Staircase F1",
    },
    "Landing" : {
        "north" : "Staircase F2",
        "east" : "Storage",
        "west" : "Guest Bedroom",
        "south" : "Hallway",
    },
    "Hallway" : {
        "north" : "Landing",
        "east" : "Upstairs Bathoom",
        "west" : "Master Bedroom",
    },
    "Guest Bedroom" : {
        "east" : "Landing",
    },
    "Storage" : {
        "west" : "Landing",
    },
    "Upstairs Bathoom" : {
        "west" : "Hallway",
    },
    "Master Bedroom" : {
        "east" : "Hallway",
        "up" : "Attic",
    },
    "Attic" : {
        "down" : "Master Bedroom"
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
    
    
