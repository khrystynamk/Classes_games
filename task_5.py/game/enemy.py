"""
Module for class of enemies.
"""

from game.character import Character


class Enemy(Character):
    """
    Class for enemies (using inheritance from class Character).
    """

    def __init__(self, name, description) -> None:
        """
        Initialyzing attributes of the class.
        """
        super().__init__(name, description)
        self.defeated = 0

    def fight(self, item):
        """
        Fight with the enemy and check whether you can defeat him.
        """
        if item == self.weakness:
            self.defeated += 1
            print(f"You fend {self.name} off with the {item}")
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self):
        """
        Return the number of victories.
        """
        return self.defeated
