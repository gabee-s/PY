'''[PY-A08] Você está desenvolvendo um programa para gerenciar uma lista de compras. O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista. Além disso, o programa calcula o valor total de todos os produtos da lista.

O programa oferece as seguintes opções:

Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.

Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.

Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.

Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.

Encerrar programa: Encerra a execução do programa.

O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.

A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.'''

# GERENCIADOR DE LISTA DE COMPRAS

#Adicionar produtos a lista
#visualizar a lista de produtos 
#atualizar as informações de um produto
#remover produtos
#calcula o valor total de todos os produtos



def adicionarProd(listaProdutos):
    produto = input('\nInforme o produto: ').title()
    valor = float(input('Informe o VALOR UNITÁRIO do produto em R$: '))
    qtd = int(input('Informe a QUANTIDADE do produto: '))
    total = valor * qtd

    dicionario = {
        'Produto': produto,
        'Valor': valor,
        'Quantidade': qtd,
        'Total': total
    }
    listaProdutos.append(dicionario)
       


def removerProd(listaProdutos):
    prodRemovido = input('\nforme o nome do produto que deseja remover: ').title()
    for dicionario in listaProdutos:
        if dicionario.get('Produto') == prodRemovido:
            listaProdutos.remove(dicionario)

def attProd(listaProdutos):
    prodAtt = input('\nInforme o nome do produto que deseja atualizar: ').title()
    for dicionario in listaProdutos:
        if dicionario.get('Produto') == prodAtt:
            novoProd = input('Informe qual será o nome do novo produto: ').title()
            novoValor = float(input('Informe qual será o valor (em R$) do novo produto: '))
            novoQtd = int(input('Informe qual será a nova quantidade do novo produto: '))
            novoTotal = novoValor * novoQtd
            novoDict ={
                'Produto': novoProd,
                'Valor':novoValor,
                'Quantidade':novoQtd,
                'Total':novoTotal
            }
            dicionario.update(novoDict)

def verProd(listaProdutos):
    for dicionario in listaProdutos:
        for chave , valor in dicionario.items():
            print(f'\n{chave}: {valor}')
        print('--'*30)

def calcular_valor_total(listaProdutos):
    return sum(produto['Total'] for produto in listaProdutos)

def main():
    listaProdutos = []

    while True:

        print('\n\nGERENCIADOR DE LISTA DE COMPRAS')
        print('\nEscolha sua opção abaixo')
        print('1-Adicionar Produto\n2-Remover Produto\n3-Atualizar/Editar Produto\n4-Ver Produtos na Lista\n5-Encerrar Gerenciador')


        opcao= input('\nEscolha sua Opção: ')
        if opcao == '1':
            adicionarProd(listaProdutos)
        elif opcao == '2':
            removerProd(listaProdutos)  
        elif opcao == '3':
            attProd(listaProdutos)
        elif opcao == '4':
            verProd(listaProdutos)
        elif opcao == '5':

            print('Encerrando o Programa...')
            break
        else:
            print('Opção Inválida, tente novamente!')
            continue

        verValorTotal = calcular_valor_total(listaProdutos)
        print(f'\n\nO valor TOTAL no carrinho é de: R${verValorTotal}')

