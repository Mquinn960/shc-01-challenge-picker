from generator.difficulty import Difficulty
from generator.generator_data import GeneratorData
from generator.generation.igeneration_strategy import IGenerationStrategy
from generator.generation.generation_strategy_factory import GenerationStrategyFactory

class Generator():

    _data: GeneratorData = None
    _generation_strategy: IGenerationStrategy = None

    def __init__(self, data: GeneratorData):
        self._data = data
        self._generation_strategy = self._initialise_generator()

    def generate_challenge(self, difficulty, challenge):

        find_challenge = [x for x in self._data.objectives if x['name'] == challenge]
        if find_challenge:
            challenge = find_challenge[0]

        difficulty_type = Difficulty[difficulty.upper()]
        return self._generation_strategy.generate(difficulty_type, challenge)

    def _initialise_generator(self) -> IGenerationStrategy:
        _generation_strategy_factory = GenerationStrategyFactory(self._data.objectives, self._data.modifiers)
        return _generation_strategy_factory.resolve_generation_strategy(self._data.generator_type)
