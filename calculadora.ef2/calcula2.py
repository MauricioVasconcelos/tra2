# calculadora.py
# Refatorado por Mauricio Vasconcelos

def calcular_preco_com_desconto(preco_original, taxa_desconto):
    """
    Calcula o preço com desconto aplicado.

    :param preco_original: float - Preço original do produto.
    :param taxa_desconto: float - Taxa de desconto a ser aplicada.
    :return: float - Preço com desconto.
    """
    return preco_original - (preco_original * taxa_desconto / 100)

def obter_preco_e_desconto():
    """
    Obtém o preço e a taxa de desconto do usuário.

    :return: tuple - Preço original e taxa de desconto.
    """
    preco = float(input("Digite o preço: "))
    taxa_desconto = float(input("Digite a porcentagem de desconto: "))
    return preco, taxa_desconto

def main():
    preco, taxa_desconto = obter_preco_e_desconto()
    preco_final = calcular_preco_com_desconto(preco, taxa_desconto)
    print(f"O preço final com desconto é: {preco_final}")

if __name__ == "__main__":
    main()
