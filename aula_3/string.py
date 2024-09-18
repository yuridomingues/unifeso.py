# Poor exemple code

 lista = {1, 2, 3} * 5
 for i, numero in enumerate (lista):
     if i < len (lista)-1:
     print (str(numero), end = ', ')
 else:
     print (str(numero), end = '')

# Good code

lista = {1, 2, 3} * 5
lista_str = [str(i) for i in lista]

resultado = ",".join(lista_str)


