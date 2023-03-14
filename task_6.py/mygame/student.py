"""
Module for Student class.
"""
from mygame.friend import Friend


class Student(Friend):
    """
    Class for Student (using inheritance from class Friend).
    """

    def __init__(self) -> None:
        """
        Initialyzing attributes of the class.
        """
        super().__init__(
            "Student",
            "A sleep-deprived creature, who would do anything for a cup of coffee.",
        )
        self.set_conversation(
            "I don't think there will be enough fingers on my hands\
 to count how many deadlines I have this week. I need coffee immediately!"
        )
