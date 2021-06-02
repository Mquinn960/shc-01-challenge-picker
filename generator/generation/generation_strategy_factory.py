from generator.generation.igeneration_strategy import IGenerationStrategy
from typing import List

from generator.generation.naive_generation_strategy import NaiveGenerationStrategy

class GenerationStrategyFactory():

    _objectives = None
    _modifiers = None

    def __init__(self, objectives: List, modifiers: List):
        self._objectives = objectives 
        self._modifiers = modifiers

    def resolve_generation_strategy(self, method: str) -> IGenerationStrategy:

        if (method == 'naive'):
            return NaiveGenerationStrategy(self._objectives, self._modifiers)
        else:
            return NaiveGenerationStrategy(self._objectives, self._modifiers)
