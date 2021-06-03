from typing import List

from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.generation.intuitive_generation_strategy import IntuitiveGenerationStrategy
from generator.generation.knapsack_generation_strategy import KnapsackGenerationStrategy

class GenerationStrategyFactory():

    _objectives = None
    _modifiers = None

    def __init__(self, objectives: List, modifiers: List):
        self._objectives = objectives 
        self._modifiers = modifiers

    def resolve_generation_strategy(self, method: str) -> IGenerationStrategy:

        if (method == 'intuitive'):
            return IntuitiveGenerationStrategy(self._objectives, self._modifiers)
        if (method == 'knapsack'):
            return KnapsackGenerationStrategy(self._objectives, self._modifiers)
        else:
            return IntuitiveGenerationStrategy(self._objectives, self._modifiers)
