from generator.generation.base_generation_strategy import BaseGenerationStrategy
from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.difficulty import Difficulty
from generator.challenge import Challenge

class KnapsackGenerationStrategy(BaseGenerationStrategy, IGenerationStrategy):

    """
    """

    def generate(self, difficulty: Difficulty, challenge: str) -> Challenge:

        

        return Challenge(challenge, self._additional_modifiers, self._current_difficulty)

