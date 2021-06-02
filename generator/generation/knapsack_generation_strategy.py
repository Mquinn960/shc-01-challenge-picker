from generator.generation.base_generation_strategy import BaseGenerationStrategy
from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.difficulty import Difficulty
from generator.challenge import Challenge

class KnapsackGenerationStrategy(BaseGenerationStrategy, IGenerationStrategy):

    """
    """

    def generate(self, difficulty: Difficulty, challenge: str) -> Challenge:

        def knapSack(W, wt, n):
    
            if n == 0 or W == 0:
                return 0
        
            if (wt[n-1]['modifier'] > W):
                return knapSack(W, wt, n-1)
        
            else:
                return knapSack(W, wt, n-1)

        def subsetsum(array, num):
            if sum([x['modifier'] for x in array]) == num:
                return array
            if len(array) > 1:
                for subset in (array[:-1], array[1:]):
                    result = subsetsum(subset, num)
                    if result is not None:
                        return result

        y = subsetsum(self._modifiers, difficulty.value)

        x = knapSack(difficulty.value, self._modifiers, len(self._modifiers))

        return Challenge(challenge, self._additional_modifiers, self._current_difficulty)

    