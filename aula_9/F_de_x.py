# F = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...}

def F_de_x(x): 
    if x == 1: 
        return 0
    if x == 2:
        return 1
    if x > 2: 
        return F(x-1) + F(x-2)
    
print(F_de_x(10))