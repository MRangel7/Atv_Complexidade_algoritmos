def busca_linear(lista, elemento):
    """
    Realiza uma busca linear em uma lista.

    Complexidade:
    - Tempo: O(n) -> precisa percorrer toda a lista no pior caso.
    - Espaço: O(1)

    Gerado e validado com auxílio do Gemini CLI.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


# Teste
numeros = [3, 7, 2, 9, 5]
print(busca_linear(numeros, 9))   # Saída esperada: 3
print(busca_linear(numeros, 10))  # Saída esperada: -1
