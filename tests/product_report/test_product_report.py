from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # Seu teste deve ser escrito aqui
    product = Product(
        10,
        "Titanium Dioxide",
        "Target Corporation",
        "2020-12-08",
        "2023-12-08",
        "FR295791533358XRG4PRIG28D08",
        "instrucao 10",
    )

    product_string = product.__str__()

    assert product_string == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
