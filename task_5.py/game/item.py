"""
Module for class of items.
"""


class Item:
    """
    Class for items.
    """

    def __init__(self, name) -> None:
        """
        Initialyzing attributes of the class.
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        Set the description for the object (Room).
        """
        self.description = description

    def get_name(self):
        """
        Return the name of an item.
        """
        return self.name

    def describe(self):
        """
        Return the description of an item.
        """
        print(f"The [{self.name}] is here - {self.description}")
        return self.description
