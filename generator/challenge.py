class Challenge():

    _objective = None
    _modifiers = None
    _difficulty = 0

    def __init__(self, objective, modifiers, difficulty):
        self._objective = objective
        self._modifiers = modifiers
        self._difficulty = difficulty

    def get_challenge(self):
        challenge_description = f"{self._objective['name']} (difficulty: {self._difficulty})"
        for modifier in self._modifiers:
            challenge_description += f" [{modifier['name']}]"
        return challenge_description

    def _has_modifiers(self):
        return self._modifiers
