from funcs_alunos import *

while True:
    exibir_menu()
    op=int(input('\n\nDigite sua escolha: '))
    if op == 5:
        print('Encerrando sistema')
        break
    elif 1<= op <= 4:
        opcoes(op)
    