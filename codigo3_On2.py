def bubble_sort(lista):
    """
    Ordena uma lista usando o algoritmo Bubble Sort.

    Complexidade:
    - Tempo: O(n²) -> dois loops aninhados.
    - Espaço: O(1)

    Gerado com auxílio do Gemini CLI.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# Teste
valores = [5, 1, 4, 2, 8]
print(bubble_sort(valores))  # Saída esperada: [1, 2, 4, 5, 8]
