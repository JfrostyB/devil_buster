currentRoom = "Entrance"

rooms = {
    "Entrance" : {
        "south": "Hall"
    },
    "Hall": {
        "north": "Entrance"
        "east" : ""
    }
}

while True:

    move = input(">")

    move = move.split(" ", 1)