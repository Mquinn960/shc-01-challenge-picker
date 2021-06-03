import random

from generator.subset_finder import SubsetFinder
from generator.generation.base_generation_strategy import BaseGenerationStrategy
from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.difficulty import Difficulty
from generator.challenge import Challenge

class IntuitiveGenerationStrategy(BaseGenerationStrategy, IGenerationStrategy):

    """
    This is an intutive generation strategy - which basically means it's
    my guess at a semi-sensible approach for defining random challenges with
    modifiers.

    Rationale/pseudocode for this intuitive generator:

    Randomly pick a challenge if one is not given

    If it's less than the target difficulty
        If <variable: 80%> chance to pick either a stack or a platform
            pick a random modifier
                add to the challenge difficulty
                If it's still below target difficulty
                    add the opposing modifier
                    If it's still below target difficulty
                        add an exotic modifier
        Else
            add an exotic modifier

    If there's still remaining space, option to fill it with
    the best matching modifier.      

    Submit challenge with 0-n modifiers
    """

    _stack_preference_weighting = 0.8
    _fill_space = True
    _current_difficulty = 0
    _additional_modifiers = []

    def generate(self, difficulty: Difficulty, challenge: str) -> Challenge:

        self._additional_modifiers = []
        self._current_difficulty = 0
        modifier_types = ['stacks', 'platforms']

        if not challenge:
            challenge = self._select_challenge(difficulty)
        self._current_difficulty += challenge['difficulty']

        if self._current_difficulty < difficulty.value:
            if self._prefer_stack_platform():
                modifier_type = random.choice(modifier_types)
                modifier_types.remove(modifier_type)
                self._add_conditional_modifier(modifier_type, difficulty)
                if self._current_difficulty < difficulty.value:
                    alternative_modifier = random.choice(modifier_types)
                    self._add_conditional_modifier(alternative_modifier, difficulty)
                    if self._current_difficulty < difficulty.value:
                        self._add_conditional_modifier('modifiers', difficulty)
            else:
                self._add_conditional_modifier('modifiers', difficulty)

        if self._fill_space:
            subset_finder = SubsetFinder()
            available_capacity = difficulty.value - self._current_difficulty
            remaining_modifiers = self._modifiers.copy()
            for modifier in self._additional_modifiers:
                remaining_modifiers.remove(modifier)
            filler_modifiers = subset_finder.find_subset(remaining_modifiers, available_capacity)
            if filler_modifiers:
                self._additional_modifiers.extend(filler_modifiers)

        return Challenge(challenge, self._additional_modifiers, self._current_difficulty)

    def _add_conditional_modifier(self, modifier_type, difficulty):
        additional_modifier = self._select_modifier(modifier_type, difficulty)
        if additional_modifier:
            self._current_difficulty += additional_modifier['modifier']
            self._additional_modifiers.append(additional_modifier)

    def _select_modifier(self, modifier_type, difficulty):

        specified_modifiers = [x for x in self._modifiers if x['type'] == modifier_type]

        exhaustion = len(specified_modifiers)
        attempts = 0

        while attempts < exhaustion:
            choice = random.choice(specified_modifiers)
            if (self._current_difficulty + choice['modifier']) < difficulty.value:
                return choice
            attempts += 1

        return None

    def _select_challenge(self, difficulty):

        exhaustion = len(self._challenges)
        attempts = 0

        while attempts < exhaustion:
            choice = random.choice(self._challenges)
            if choice['difficulty'] <= difficulty.value:
                return choice
            attempts += 1

        raise Exception("Exhaustion reached - no suitable challenges in database for this difficulty")

    def _prefer_stack_platform(self):
        preference_chance = random.uniform(0, 1)
        return preference_chance <= self._stack_preference_weighting
