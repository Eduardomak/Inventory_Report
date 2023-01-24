from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.find("xml") == -1:
            raise ValueError("Arquivo inválido")

        else:
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
