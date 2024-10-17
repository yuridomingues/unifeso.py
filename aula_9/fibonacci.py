def fibonacci(n: int) -> int:
    a: int = 0
    b: int = 1

    if n == 1:
        return a
    if n == 2:
        return b
    
    soma : int = 0
    for i in range(2, n):
        soma = a + b
        a = b
        b = soma
        
    return soma

if __name__ == '__main__':   
    print(f"{fibonacci(8):,}")