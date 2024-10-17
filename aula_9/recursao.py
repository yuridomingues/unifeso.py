def recursao (n: int) -> int:

    # Caso base
    if n == 1:
        return n
    # Caso recursivo
    else:
        return n * recursao(n - 1)
    # Se n = 5, a função recursao(5) = 5 * recursao(4)
    # recursao(4) = 4 * recursao(3)
    # recursao(3) = 3 * recursao(2)
    # recursao(2) = 2 * recursao(1)
    # recursao(1) = 1
    # recursao(2) = 2 * 1 = 2
    # recursao(3) = 3 * 2 = 6
    # recursao(4) = 4 * 6 = 24
    # recursao(5) = 5 * 24 = 120
    