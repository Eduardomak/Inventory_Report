from csv import DictReader
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.find("csv") == -1:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            return list(DictReader(file))
