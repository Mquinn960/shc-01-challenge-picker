from .generator_data import GeneratorData

class Generator():

    _data: GeneratorData = None

    def __init__(self, data: GeneratorData):
        self._data = data

    def generate_challenge(self, difficulty, challenge):

        if self._data.generator_type == 'naive':
            pass

        return None
