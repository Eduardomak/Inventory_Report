from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    # Seu teste deve ser escrito aqui

    product = [
        {
            "id": "10",
            "nome_do_produto": "Titanium Dioxide",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-08",
            "data_de_validade": "2023-12-08",
            "numero_de_serie": "FR295791533358XRG4PRIG28D08",
            "instrucoes_de_armazenamento": "instrucao 10",
        },
    ]
    complete_report = ColoredReport(CompleteReport).generate(product)
    """ print(complete_report)
    print("\033[32mData de fabricação mais antiga: \033[36m2020-12-08") """
    assert ("\033[36m" in complete_report) is True
    assert ("\033[32m" in complete_report) is True
    assert ("\033[31m" in complete_report) is True
