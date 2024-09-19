## Introdução às Collections;

Listas(Lists);
Tuplas (Tuples);
Conjuntos (Sets);
Dicionários (Dictionaries);

Collections Epsecializadas:

* Counter
* defaultdict
* ordereddict
* namedtuple

Arrays
Comparação entre Collections;

Exercicios Práticos:

Array é uma coleção de elementos do mesmo tipo, N elementos, variando de 0 até o quanto a memória suportar 

Pra que criamos array?
Para armazenar uma quantidade N de elementos em um só local, mas pegam bastante memória. 4 bytes de memória para cada caractere de uma array

O que são listas?

Tem 2 coisas que arrays não tem, eles são heterogeneos, pode armazenar numa mesma lista um inteiro, uma string, um booleano, uma propria lista, uma tupla, um dicionario, pode colocar qualquer coisa.

Para criar uma lista em Python:

Lista = []

Exemplo: 

my_list [0,1,2] // lista homogenea
my_list [] // lista vazia
my_list [20, 3,14, true, [1, 2, 3]]

para pegar true
my_list [2]
my_list [4] // da erro
my_list[3] // print [1,2,3]

my_list [1:3] // vai printar os caracteres 1, 2 e 3, slicing

Em um slicing, se usa 
Indice inicial : Indice final

Para pegar o último elemento sem você saber o final seria: 
print(lista[-1])

Como se debuga em python? 

quit -> encerra o programa

Listas, métodos principais

- append(x): Adiciona um item ao final;
- extend(iterable): Adiciona todos os itens do iterável;
- insert(i, x): Insere um item em uma posição específica;
- remove(x): Remove a primeira ocorrência de um item;
- pop([i]): Remove e retorna o item em uma posição (ou o último);
- sort(): Ordena a lista in-place;
- reverse(): Inverte a ordem dos elementos.

Pilha -> last-in/first-out(lifo)

- O ultimo que entra, sai primeiro (pop)

