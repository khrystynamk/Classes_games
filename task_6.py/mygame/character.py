"""
Module for class of characters (enemy and friend as iheritants).
"""

class Character:
    """
    Class for characters.
    """

    def __init__(self, name, description) -> None:
        """
        Initialyzing attributes of the class.
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.wanted_item = None
        self.torba = []

    def set_conversation(self, conversation):
        """
        Set the conversation for the character.
        """
        self.conversation = conversation

    def describe(self):
        """
        Return the description of the character.
        """
        print(self.name)
        print(self.description)

    def set_wanted_item(self, wanted_item):
        """
        Set weakness for the enemy (Character).
        """
        self.wanted_item = wanted_item

    def talk(self):
        """
        Return the conversation with the character.
        """
        print(f"[{self.name} says]: {self.conversation}")

    def give(self, item):
        """
        Give item from torba to certain character.
        """
        if any(item_in_torba.name == item for item_in_torba in self.torba):
            print(f"[{self.name} says]: Here, please take {item}.")
            return True
        print(f"Sorry, I do not have {item}. Please don't hit me!")
        return False
