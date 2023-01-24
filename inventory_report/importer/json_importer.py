from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.find("json") == -1:
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                return json.load(file)
