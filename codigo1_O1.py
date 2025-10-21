def get_first_element(lista):
    """
    Retorna o primeiro elemento de uma lista.

    Complexidade:
    - Tempo: O(1) -> constante, pois o acesso a um índice é imediato.
    - Espaço: O(1)

    Gerado e testado com auxílio do Gemini CLI.
    """
    return lista[0] if lista else None


# Teste
lista = [10, 20, 30, 40]
print(get_first_element(lista))  # Saída esperada: 10
