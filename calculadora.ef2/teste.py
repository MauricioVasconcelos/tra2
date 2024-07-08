# test_calculadora.py
# Testes criados por Mauricio Vasconcelos

import pytest
from calculadora import calcular_preco_com_desconto

def test_calcular_preco_com_desconto():
    assert calcular_preco_com_desconto(100, 10) == 90
    assert calcular_preco_com_desconto(200, 20) == 160
    assert calcular_preco_com_desconto(0, 10) == 0
    assert calcular_preco_com_desconto(100, 0) == 100

if __name__ == "__main__":
    pytest.main()

