'''[PY-A03] Crie um programa em Python que permita adicionar,
remover e visualizar alunos e seus números de matrícula usando um dicionário.

O programa deve fornecer as seguintes funcionalidades:

Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.

Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.

Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário,
exibindo seus respectivos números de matrícula.

O programa deve ser executado em um loop contínuo até que o usuário escolha sair.'''

banco={}
while True:
        print('O que deseja fazer ?')
        print('1- Adicionar Aluno\n2- Remover Aluno\n3- Visualizar Alunos Registrados\n4- Encerrar Programa')
        controle=int(input('Digite o número da opção que escolher: '))
        if controle == 1:

            nome=input('Digite o primeiro nome do(a) aluno(a): ').capitalize()
            sobrenome=input('Digite sobrenome do(a aluno(a):  ').capitalize()
            nome_completo=nome+' '+sobrenome

            matricula=int(input('Insira o número de Matrícula: '))
            banco.update({nome_completo:matricula})

        elif controle == 2:

            removido=int(input('Digite a matrícula do Aluno que deseja remover: '))
            remover_chave=[chave for chave, valor in banco.items() if valor==removido]
            for chave in remover_chave:
                del banco[chave]

        elif controle == 3:

            for chave,valor in banco.items():
                print(f'{chave}-{valor}')

        elif controle==4:
            break
        else:
            print('Opção Inválida')
            continue