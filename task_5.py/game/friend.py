"""
An additional module for class of friends,
which is not used in this task, but will be used in task 6.
"""
from game.character import Character
from game.room import Room
from game.enemy import Enemy


class Friend(Character):
    """
    Class for friends (using inheritance from class Character).
    """

    def recommend_weapon(self, other: Enemy):
        """
        Your friend recommends, which weapon to use against the enemy.
        """
        print(
            f"[{self.name} says]: You should use {other.weakness} to defeat this enemy!"
        )

    def notify_of_danger(self, other: Room):
        """
        Your friend notifies you about the danger in the room you are about to enter.
        """
        monster = other.get_character()
        if monster is not None and isinstance(monster, Enemy):
            print(
                f"[{self.name} says]: There is a monster in this room,\
 are you really sure you want to go there? (Y/N)"
            )
        else:
            print(
                f"[{self.name} says]: The room is safe to be entered!"
            )
