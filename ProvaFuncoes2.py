'''[PY-A05] Considere uma lista de números inteiros 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

-Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

-Função filter() para obter uma nova lista com números pares da lista numeros

-Função reduce()  para obter a soma de todos os números da lista numeros

Qual o resultado obtido após a execução das operações acima?'''

from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados=list(map(lambda num:num**2,numeros))
pares=list(filter(lambda num:num%2==0,numeros))
soma=reduce(lambda num1,num2:num1+num2,numeros)

print(f'O quadrado de cada número é:{quadrados}\nOs números pares são:{pares}\nA soma de todos é:{soma}')
