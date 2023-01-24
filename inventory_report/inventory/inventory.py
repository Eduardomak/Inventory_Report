from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import json
import xmltodict
from csv import DictReader


class Inventory:
    @staticmethod
    def create_report(data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @staticmethod
    def import_data(path, report_type):
        if path.find("csv") != -1:
            with open(path) as file:
                data = list(DictReader(file))
                return Inventory.create_report(data, report_type)

        elif path.find("json") != -1:
            with open(path) as file:
                data = json.load(file)
                return Inventory.create_report(data, report_type)

        elif path.find("xml") != -1:
            with open(path) as file:
                data = xmltodict.parse(file.read())["dataset"]["record"]
                return Inventory.create_report(data, report_type)

        else:
            raise ValueError("File format must be json, xml or csv")
