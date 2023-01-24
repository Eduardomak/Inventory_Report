from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def file_type(path):
    if path.find("csv") != -1:
        return CsvImporter
    elif path.find("json") != -1:
        return JsonImporter
    elif path.find("xml") != -1:
        return XmlImporter
    else:
        raise NotImplementedError


def main():
    if len(sys.argv) < 3:
        print(ValueError("Verifique os argumentos"), file=sys.stderr)
        return

    *_, path, type = sys.argv
    file = file_type(path)
    final_report = InventoryRefactor(file).import_data(path, type)
    print(final_report, end="")
