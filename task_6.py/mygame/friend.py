"""
Module for Friend class.
"""
from mygame.character import Character
from mygame.street import Street
from mygame.enemy import Enemy


class Friend(Character):
    """
    Class of friends.
    """

    def notify_of_danger(self, other: Street):
        """
        Your friend notifies you about the danger on the street you are about to go to.
        """
        monster = other.get_character()
        if monster is not None and isinstance(monster, Enemy):
            print(
                f"[{self.name} says]: There is a dangerous person on this street,\
 are you really sure you want to go there? (Y/N)"
            )
        else:
            print(f"[{self.name} says]: The street is safe!")
