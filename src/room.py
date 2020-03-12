# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room(Item):
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += f"Currently in: {self.name}"
        return_string += "\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += "Items in room: "
        return_string += ", ".join(x for x in self.getItemNames())
        return_string += "\n"
        return_string += f"{self.get_exits_string()}"
        return return_string

    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def getItemNames(self):
        return [item[0] for item in self.items]

    def getItemDescriptions(self):
        return [item[1] for item in self.items]
