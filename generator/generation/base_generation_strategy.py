from typing import List

from generator.generation.igeneration_strategy import IGenerationStrategy

class BaseGenerationStrategy(IGenerationStrategy):

    _challenges = []
    _modifiers = []

    def __init__(self, challenges: List, modifiers: List):
        self._challenges = challenges
        self._modifiers = modifiers

    @property
    def challenges(self):
        return self._challenges
    
    @property
    def modifiers(self):
        return self._modifiers
