lista1 = [1,2,3]
lista1.append(4) # Adiciona o elemento 4 no final da lista
lista2 = [41,10,12,54,22,30]

lista1.extend(lista2) # Adiciona os elementos da lista2 no final da lista1
print(lista1)

lista1.remove(10) # Remove o número 10 da lista, usando do valor
print(lista1)

lista1.pop(3) # Remove o elemento na posição 3 da lista
print(lista1)

numero_a_remover = 41 

if numero_a_remover in lista1:
    lista1.remove(numero_a_remover) # Remove o número 41 da lista, usando o valor
print (lista1)

