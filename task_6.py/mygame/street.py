"""
Module for class of stree.
"""

from mygame.character import Character


class Street:
    """
    Class for street.
    """

    def __init__(self, name) -> None:
        """
        Initialyzing attributes of the class.
        """
        self.name = name
        self.street_links = {}
        self.description = None
        self.item = None
        self.character = None

    def set_description(self, description):
        """
        Set the description for the object (Street).
        """
        self.description = description

    def link_street(self, street: "Street"):
        """
        Adding street to the dictionary of links.
        """
        self.street_links[street.name] = street
    

    def get_destinations(self):
        """
        Return list of possible destinations
        """
        return self.street_links.keys()

    def set_item(self, item):
        """
        Set the item for the object (Street).
        """
        self.item = item

    def set_character(self, character: Character):
        """
        Set the character for the object (Street).
        """
        self.character = character

    def move(self, next_move):
        """
        Move to the next location.
        """
        if next_move in self.street_links:
            return self.street_links[next_move]
        return "There is no such direction!"

    def get_details(self):
        """
        Return the description and details of the street.
        """
        print(self.name)
        print("-" * 20)
        print(self.description)
        sorted_links = sorted(self.street_links.items(), key=lambda x: x[1].name)
        for key, _ in sorted_links:
            print(f"You can go to '{key}'")
        return self.description

    def get_character(self):
        """
        Return the character, which is on the Street.
        """
        return self.character

    def get_item(self):
        """
        Return the item, which is located on particular Street.
        """
        return self.item
