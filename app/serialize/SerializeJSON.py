import json


class SerializeJSON():
    @staticmethod
    def convert(input_data: list):

        return json.dumps(input_data)