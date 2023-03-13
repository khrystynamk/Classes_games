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
        self.weakness = None

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

    def set_weakness(self, weakness):
        """
        Set weakness for the enemy (Character).
        """
        self.weakness = weakness

    def talk(self):
        """
        Return the conversation with the character.
        """
        print(f"[{self.name} says]: {self.conversation}")
