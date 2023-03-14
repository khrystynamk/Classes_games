"""
Module for Cavalier class.
"""
from mygame.friend import Friend


class Cavalier(Friend):
    """
    Class for Cavalier (using inheritance from class Friend).
    """

    def __init__(self):
        """
        Initialyzing attributes of the class.
        """
        super().__init__(
            "Cavalier", "A charming friend of yours who always tries to take you out."
        )
        self.set_conversation(
            "Hey, do you feel like going for a coffee?\
 I will accept no other answer, but a positive one."
        )
