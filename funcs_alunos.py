'''[PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:


AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.

Lembre Se de Modularizar o código'''

alunos = {}



def AdicionarAluno():
    valor= input('\nDigite o nome do aluno: ').title()
    while True:
        chave= input('Digite a matrícula do aluno: ')
        if chave in alunos:
            print('\nMatrícula já Cadastrada, Tente Novamente.')
            continue
        elif chave not in alunos:
            alunos.update({chave:valor}) 
            print('\nAluno Adicionado com Sucesso!')
            break

def RemoverAluno():
    while True:
        remover_aluno= input('\nDigite a matrícula do aluno que deseja remover: ')
        if remover_aluno not in alunos:
            print('Aluno não encontrado!')
            continue
        elif remover_aluno in alunos:
            del alunos[remover_aluno]
            print('\nAluno Removido com Sucesso!')
            break

def AtualizarAluno():
    while True:
        mat_aluno=input('Digite a matrícula do aluno que deseja atualizar: ')
        if mat_aluno in alunos:
            att_aluno= input('\nDigite o novo nome do aluno: ')
            alunos.update({mat_aluno:att_aluno})
            print('\nNome Atualizado com Sucesso')
            break
        else:
            print('\nAluno não encontrado\nTente Novamente\n')
            continue

def VerAlunos():
    print('\nLISTA DE ALUNOS:\n\n')
    for chave,valor in alunos.items():
        print(f'\nMatrícula:{chave}\nAluno:{valor}\n\n')
    print('#'*60,'\nFim da Lista De Alunos')

def exibir_menu():
    print('\nPROGRAMA DE CADASTRO DE ALUNOS!')
    print('Escolha uma das opções abaixo:\n\n')
    print('1-Adicionar Aluno(a)\n2-Remover Aluno(a)\n3-Atualizar Aluno(a)\n4-Ver Lista de Alunos\n5-Encerrar Programa')

def opcoes(escolha_usuario):
    if escolha_usuario == 1:
        AdicionarAluno()
    elif escolha_usuario == 2:
        RemoverAluno()
    elif escolha_usuario == 3:
        AtualizarAluno()
    elif escolha_usuario == 4:
        VerAlunos()
    else:
        print('Opção inválida')

