# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("\nThere is no room in that direction.")

    def printInventory(self):
        print(f"\nYour inventory: {[item[0] for item in self.inventory]}")

    def getInventory(self):
        return [item[0] for item in self.inventory]

    def getItem(self, item):
        if item in self.current_room.getItemNames():
            position = self.current_room.getItemNames().index(item)
            self.inventory.append(self.current_room.items[self.current_room.getItemNames().index(item)])
            self.current_room.items.pop(position)
            print(f"\nYou got {item}\n")
            print(self.current_room)
        else:
            print(f"\nYou cannot take {item} because it's not in this room.")

    def dropItem(self, item):
        if item in self.getInventory():
            position = self.getInventory().index(item)
            self.current_room.items.append(self.inventory[self.getInventory().index(item)])
            self.inventory.pop(position)
            print(f"\nYou dropped {item}\n")
            print(self.current_room)
        else:
            print(f"\nYou cannot drop {item} because you don't have it.")
