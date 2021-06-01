import json

class Reader():

    def read_from_json(self, read_path):
        try:
            with open(read_path) as json_file:
                return json.load(json_file)
        except Exception as e:
            print(f'File reading error: {e}')
