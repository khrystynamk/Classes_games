"""
Module for class of rooms.
"""

from game.character import Character


class Room:
    """
    Class for rooms.
    """

    def __init__(self, name) -> None:
        """
        Initialyzing attributes of the class.
        """
        self.name = name
        self.room_links = {}
        self.description = None
        self.item = None
        self.character = None

    def set_description(self, description):
        """
        Set the description for the object (Room).
        """
        self.description = description

    def link_room(self, room: object, link):
        """
        Adding rooms to the dictionary of links.
        """
        self.room_links[link] = room

    def set_item(self, item):
        """
        Set the item for the object (Room).
        """
        self.item = item

    def set_character(self, character: Character):
        """
        Set the character for the object (Room).
        """
        self.character = character

    def move(self, next_move):
        """
        Move to the next location.
        """
        if next_move in self.room_links:
            return self.room_links[next_move]
        return "There is no such direction!"

    def get_details(self):
        """
        Return the description and details of the room.
        """
        print(self.name)
        print("-" * 20)
        print(self.description)
        sorted_links = sorted(self.room_links.items(), key=lambda x: x[1].name)
        for key, value in sorted_links:
            print(f"The {value.name} is {key}")
        return self.description

    def get_character(self):
        """
        Return the character, which is inside the room.
        """
        return self.character

    def get_item(self):
        """
        Return the item, which is inside the particular room.
        """
        return self.item
