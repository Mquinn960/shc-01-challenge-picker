class Challenge():

    _objective = None
    _modifiers = None

    def __init__(self, objective, modifiers):
        self._objective = objective
        self._modifiers = modifiers

    def get_challenge(self):
        print("Challenge!")
