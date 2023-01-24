from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):

        oldest_date = min([_["data_de_fabricacao"] for _ in data])

        now_date = datetime.now()

        """ now_date = "2023-01-10" """

        closest_date = min(
            [
                _["data_de_validade"]
                for _ in data
                if datetime.strptime(_["data_de_validade"], "%Y-%m-%d")
                > now_date
            ]
        )

        company_bigger_stock_number = Counter(
            [_["nome_da_empresa"] for _ in data]
        ).most_common()[0]

        company_bigger_stock, _ = company_bigger_stock_number

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
