import random, math

from generator.generation.base_generation_strategy import BaseGenerationStrategy
from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.subset_finder import SubsetFinder
from generator.difficulty import Difficulty
from generator.challenge import Challenge

class KnapsackGenerationStrategy(BaseGenerationStrategy, IGenerationStrategy):

    """
    This is a pseudo knapsack generation strategy (we don't have values associated)
    with modifiers - only detractors (weighting).

    Uses subset sums to optimally select the closest pair to the desired weighting
    at the desired number of modifiers, working backwards if there is no applicable
    set of modifiers that satisfies the criteria.
    """

    _desired_modifier_count = 3

    def generate(self, difficulty: Difficulty, challenge: str) -> Challenge:

        subset_finder = SubsetFinder()
        modifiers = []
        actual_modifier_count = 0

        if not challenge:
             challenge = self._select_challenge(difficulty)

        available_capacity = difficulty.value - challenge['difficulty']
        continue_optimisation = True

        if available_capacity > 0:
            if self._desired_modifier_count > 1:
                while self._desired_modifier_count > 1 and continue_optimisation and actual_modifier_count < self._desired_modifier_count:
                    temp_modifiers = self._modifiers.copy()
                    for i in range(self._desired_modifier_count):
                        aggregated_modifiers = []
                        capacity = math.floor(available_capacity / self._desired_modifier_count)
                        additional_subset = subset_finder.find_subset(temp_modifiers, capacity)
                        if additional_subset:
                            aggregated_modifiers.extend(subset_finder.find_subset(temp_modifiers, capacity))
                        if aggregated_modifiers:
                            for modifier in aggregated_modifiers:
                                temp_modifiers.remove(modifier)
                            modifiers.extend(aggregated_modifiers)
                            actual_modifier_count =+ len(modifiers)
                    if modifiers:
                        continue_optimisation = False
                    else:
                        self._desired_modifier_count -= 1
            else:
                modifiers = subset_finder.find_subset(self._modifiers, available_capacity)

        current_difficulty = challenge['difficulty'] + sum([x['modifier'] for x in modifiers])

        return Challenge(challenge, modifiers, current_difficulty)

    def _select_challenge(self, difficulty):

        exhaustion = len(self._challenges)
        attempts = 0

        while attempts < exhaustion:
            choice = random.choice(self._challenges)
            if choice['difficulty'] <= difficulty.value:
                return choice
            attempts += 1

        raise Exception("Exhaustion reached - no suitable challenges in database for this difficulty")
