from config import Config

class GeneratorData():

    _base_config: Config = None
    _no_experience_modifier = 7

    _objectives = []
    _modifiers = []

    def __init__(self, config: Config):
        self._base_config = config
        self._compile_objectives()
        self._compile_modifiers()

    @property
    def generator_type(self):
        return self._base_config.generator_type

    @property
    def objectives(self):
        return self._objectives

    @property
    def modifiers(self):
        return self._modifiers

    def _compile_objectives(self):
        self._objectives = self._base_config.objectives

    def _compile_modifiers(self):

        combined_modifiers = []
        difficulty_scale = self._base_config.difficulty_scale

        participant = self._base_config.get_current_participant()

        stacks = self._base_config.stacks
        platforms = self._base_config.platforms
        modifiers = self._base_config.modifiers

        # Adding modifiers which are irrespective of participant skill
        for modifier in modifiers:
            modifier['type'] = 'modifiers'
        combined_modifiers.extend(modifiers)

        # Adding tech stacks with modifier weighting based on inverse familiarity
        for stack in stacks:
            for participant_stack in participant['stacks']:
                if stack == participant_stack['name']:
                    modifier = difficulty_scale - participant_stack['familiarity']
                    combined_modifiers.append({'name': stack, 'modifier': modifier, 'type': 'stacks'})
                else:
                    combined_modifiers.append({'name': stack, 'modifier': self._no_experience_modifier, 'type': 'stacks'})

        # Adding platforms with modifier weighting based on inverse familiarity
        for platform in platforms:
            for participant_platform in participant['platforms']:
                if platform == participant_platform['name']:
                    modifier = difficulty_scale - participant_platform['familiarity']
                    combined_modifiers.append({'name': platform, 'modifier': modifier, 'type': 'platforms'})
                else:
                    combined_modifiers.append({'name': platform, 'modifier': self._no_experience_modifier, 'type': 'platforms'})

        self._modifiers = combined_modifiers
