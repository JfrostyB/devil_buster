from inventory import inventory
currentRoom = "Entrance"

rooms = {
    "Entrance"  : {
        "south": "Hall",
        "item" : "steel pipe"
    },
    "Hall 1": {
        "north": "Entrance",
        "west" : "Room 1",
        "east" : "Room 2",
        "south" : "Hall 2"
    },
    "Hall 2": {
        "north" : "Hall 1",
        "east" : "Room 3",
        "west" : "kitchen",
        "south" : "Staircase F1",
    },
    "Room 1" : {
        "east" : "Hall 1",
        "west" : "Garage",
    },
    "Garage" : {
        "east" : "Room 1",
    },
    "Room 2" : {
        "west" : "Hall 1",
    },
    "Room 3" : {
        "east" : "Hall 2",
    },
    "Kitchen" : {
        "west" : "Hall 2",
        "south" : "Backyard",
    },
    "Backyard" : {
        "north" : "Kitchen",
    },
    "Staircase F1" : {
        "north" : "Hall 2",
        "down" : "Staircase F2",
    },
    "Staircase F2" : {
        "north" : "Hall 4",
        "up" : "Staircase F1",
    },
    "Hall 4" : {
        "south" : "Staircase 2",
        "east" : "Room 5",
        "west" : "Room 4",
        "north" : "Hall 5",
    },
    "Hall 5" : {
        "south" : "Hall 4",
        "east" : "Room 6",
        "west" : "Room 7",
    },
    "Room 4" : {
        "east" : "Hall 4",
    },
    "Room 5" : {
        "west" : "Hall 4",
    },
    "Room 6" : {
        "west" : "Hall 5",
    },
    "Room 7" : {
        "east" : "Hall 5",
        "down" : "Attic",
    },
    "Attic" : {
        "up" : "Room 7"
    }
}   

print("I am in the", currentRoom)

while True:

    move = input(">")

    move = move.split(" ", 1)

    if move[0] == "get":
        if move[1] == rooms[currentRoom]["item"]:
            print(f"You picked up a {move[1]}")
            inventory.append(move[1])
            print(inventory)
