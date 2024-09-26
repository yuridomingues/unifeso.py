## Dica:

Fazer as listas de exercicios
Pegar a fácil e a média.

## Revisão da matéria

## O que é algoritmo?

Conjunto passo a passo de regras finitas que eu dou para a maquina para a maquina executar algo

## O que é programa?

Pegar a ideia do algoritmo e escrever em uma linguagem de programação qualquer, criando um programa

## Toda linguagem de programação ela obedece a tres estruturas basicas

1- Sequencia
2- Condição/Decisão
3- Repetição 

## O que é uma variavel?

Um valor armazenado na memoria do computador, precisa de tipo

Type int -> Escrever sobre na prova
Dito isso, tipar na prova

## O que é subrotina? Para que serve?

Subrotina é um termo generico referente a todo e qualquer tipo de trecho de codigo que não segue o fluxo padrão de execução do sistema
Outras palavras, trechos de código que são executados em determinados periodos de execução do código

Procedimento não retorna nada
Procedimento são subrotinas que não retornam nada

## O que é uma assinatura de uma subrotina?

Tipo de retorno
O que devolve para quem chamou
O nome dela
O que recebe de parametro

Obs: só pode ter uma por programa

## O que são os parametros?

Nome das variaveis

## Por que divido meu código em pedaços?

Organizado, legivel, ajuda na manutenção
SOLID -> PRINCIPIO DA RESPONSABILIDADE UNICA
Algo pode existir, somente com um proposito, quando começa a atribuir muitas responsabildiades para uma função/subrotina, fica um código ruim.

## Estudar sobre os tipos de variaveis em Python

Int = 10 
Float = 10.5
Como avisar o tipo?
num: int = 10 

Usar linter Python
-Ruff
-Pylance
-Flake8

Vai cair sobre range na prova
Range(inicio, fim, passo)
String = uma lista de caracteres

O fim é um intervalo aberto, enquanto ini<fim
Se fosse um final fechado seria ini <= fim

O passo vai pulando por exemplo
Passo = 1
1, 2, 3
Passo = 2
1, 3, 5

Função é tipo, tudo no python é um objeto
Vai cair if

## Exemplo de código range

Não vai cobrar indice negativo

def main() -> None:
    for num in range(0, 21, 2): 
        print(num)

if __name__ == "__main__":
    main()

    Por que retorna None?
None representa o void do C

Vai cair na prova Loop 

Quando usa while?
Quando não sabe quando vai ser o fim do loop

Quando usa for?
Quando sabe quando vai ser o fim do loop

Continue -> Pula a interação
Break -> Interrompe a interação

String = é um vetor de caracteres
For char in s

A gente cria subrotina para separar responsabilidades do codigo

Quem propos SOLID - autor do livro cleancode Robert Mart

Argumento é o que é passado
Parametro recebe um argumento