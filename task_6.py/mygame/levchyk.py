"""
Module for Levchyk class.
"""
from mygame.friend import Friend


class Levchyk(Friend):
    """
    Class for Levchyk (using inheritance from class Friend).
    """

    def __init__(self, treats: list) -> None:
        """
        Initialyzing the attributes of the class.
        """
        super().__init__("Levchyk", "The first mayor of cats in the whole world!")
        self.set_conversation("Mrrr, meow!~~~ /ᐠ-ꞈ-ᐟ\ ~~~")
        self.required_treats = treats

    def check_treats(self, treats_in_torba):
        """
        Levchyk checks if all desired treats are in torba.
        """
        names_of_treats_in_torba = [elem.name for elem in treats_in_torba]

        if all(elem.name in names_of_treats_in_torba for elem in self.required_treats):
            print("Mrrr, thank you for the treats, adventurer!")
            return True
        print("I can't believe it was such a hard thing to find all the treats! You failed!")
        return False
