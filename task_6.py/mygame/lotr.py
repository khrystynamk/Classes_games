"""
Module for Lotr class.
"""
from mygame.enemy import Enemy


class Lotr(Enemy):
    """
    Class for Lotrs (using inheritance from class Enemy).
    """

    def __init__(self):
        """
        Initialyzing attributes of the class.
        """
        super().__init__("Lotr", "An extremely hideous and dangerous thief.")
        self.set_conversation(
            "Let me take a picture of you and earn some money! Smile, dear!"
        )
