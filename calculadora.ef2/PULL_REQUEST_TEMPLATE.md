## Descrição da Alteração
Refatoração do código para aplicar práticas de Clean Code e criação de testes unitários.

## Prints de Antes e Depois
- Código sujo:
```python
def calc_desc(price, discount):
    if price > 100:
        return price - price * discount / 100
    else:
        return price - price * discount / 100
