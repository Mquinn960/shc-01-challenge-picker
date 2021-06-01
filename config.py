from data.io.reader import Reader

class Config():

    _reader = None

    _base_config = None
    _challenge_data = None
    _participants = None

    def __init__(self, base_config_path="./config.json"):
        self._reader = Reader()
        self._compile_config(base_config_path)

    def get_base_config(self):
        return self._base_config

    def get_current_participant(self):
        current_participant = self._base_config['participant']
        return self._participants[current_participant]

    @property
    def difficulty_scale(self):
        return self._base_config['difficulty_scale']

    @property
    def challenge_data(self):
        return self._challenge_data

    @property
    def objectives(self):
        return self._challenge_data['objectives']

    @property
    def stacks(self):
        return self._challenge_data['stacks']

    @property
    def platforms(self):
        return self._challenge_data['platforms']

    @property
    def modifiers(self):
        return self._challenge_data['modifiers']

    @property
    def participants(self):
        return self._participants

    def _compile_config(self, config_path):
        self._base_config = self._reader.read_from_json(config_path)
        self._parse_challenge_data()
        self._parse_participant_data()

    def _parse_challenge_data(self, config_path="./data/challenge_data_path.json"):
        
        if self._base_config['data']['challenge_data_path']:
            config_path = self._base_config['data']['challenge_data_path']
        
        self._challenge_data = self._reader.read_from_json(config_path)

    def _parse_participant_data(self, config_path="./data/participant_data_path.json"):

        if self._base_config['data']['participant_data_path']:
            config_path = self._base_config['data']['participant_data_path']
        
        self._participants = self._reader.read_from_json(config_path)
