def mult ( a: int , b: int ) -> int :
    
    # Caso base
    if b == 0 :
        return 0
    if b == 1 :
        return a
    
    # Caso recursivo 
    return a + mult ( b - 1 )
