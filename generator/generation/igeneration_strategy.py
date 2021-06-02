from abc import ABC, abstractmethod
from typing import List

from generator.difficulty import Difficulty
from generator.challenge import Challenge

class IGenerationStrategy():

    @abstractmethod
    def generate(self, difficulty: Difficulty, challenge: str) -> Challenge:
        raise NotImplementedError
