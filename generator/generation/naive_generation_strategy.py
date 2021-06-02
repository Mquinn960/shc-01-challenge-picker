from generator.generation.base_generation_strategy import BaseGenerationStrategy
from typing import List

from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.difficulty import Difficulty
from generator.challenge import Challenge

class NaiveGenerationStrategy(BaseGenerationStrategy, IGenerationStrategy):

    def generate(self, difficulty: Difficulty, challenge: str) -> Challenge:

        return Challenge(self._challenges, self._modifiers)
