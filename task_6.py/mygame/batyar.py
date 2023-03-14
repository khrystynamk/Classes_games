"""
Module for Batyar class.
"""
from mygame.enemy import Enemy


class Batyar(Enemy):
    """
    Class for Batyars (using inheritance from class Enemy).
    """

    def __init__(self):
        """
        Initialyzing attributes of the class.
        """
        super().__init__(
            "Batyar",
            "A free-spirit and adventurous Batyar, who has strange views and does unpredictable things",
        )
        self.set_conversation(
            "Hey, do you feel this boredom in the air? Let's do something crazy!"
        )
