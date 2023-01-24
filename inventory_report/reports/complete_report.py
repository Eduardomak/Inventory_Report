from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):

        simple_report = SimpleReport.generate(data)

        company_stock = {}
        for _ in data:
            if _["nome_da_empresa"] in company_stock:
                company_stock[_["nome_da_empresa"]] += 1
            else:
                company_stock[_["nome_da_empresa"]] = 1

        company_quantity = ""
        for key, quantity in company_stock.items():
            company_quantity += f"- {key}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_quantity}"
        )
