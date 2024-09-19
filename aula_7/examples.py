# Step example

lista = list(range(11))
print(lista)
print(lista[0:11:2]) # O terceiro sempre pula uma quantidade de casas

# Exemplo de omição do final

lista = list(range(11))
print(lista)
print(lista[:: -1]) # Inverte a lista
print(lista[0::2]) # Pega os números pares da lista
print(lista[1::2][::-1]) # Pega os números ímpares e inverte a lista

# Se a lista tiver 11 elementos e eu quiser printar o seguinte:

print(lista[13]) # Vai dar erro, pois não existe o índice 13

print(sorted(lista1)[::-1]) # Inverte a lista ordenada
