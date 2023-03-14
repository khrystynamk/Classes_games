"""
Module for class of enemies.
"""

from mygame.character import Character


class Enemy(Character):
    """
    Class for enemies (using inheritance from class Character).
    """
    def demand(self, character: Character):
        """
        An enemy demands a certain item from torba.
        """
        print(f"Hey you, {character.name}! I demand {self.wanted_item}!\
 Show me what you have in your torba! I see you have: ")
        for item in character.torba:
            print(item.name)
        