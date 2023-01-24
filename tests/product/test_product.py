from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        10,
        "Titanium Dioxide",
        "Target Corporation",
        "2020-12-08",
        "2023-12-08",
        "FR295791533358XRG4PRIG28D08",
        "instrucao 10",
    )
    assert product.id == 10
    assert product.nome_do_produto == "Titanium Dioxide"
    assert product.nome_da_empresa == "Target Corporation"
    assert product.data_de_fabricacao == "2020-12-08"
    assert product.data_de_validade == "2023-12-08"
    assert product.numero_de_serie == "FR295791533358XRG4PRIG28D08"
    assert product.instrucoes_de_armazenamento == "instrucao 10"
