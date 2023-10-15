'''Desenvolva um programa em Python que permita ao usuário digitar várias notas. 
Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno.
 Também crie uma função chamada "verificar_situacao" que, com base na média calculada, 
 irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7,
 e "Parabéns, sua média é 10" se a média for igual a 10.'''

lista_notas=[]
contador_notas=0
while True:
    nota=float(input('Insira a nota do aluno 0-10 (caso deseje parar, digite uma nota inválida): '))
    if 0<=nota<=10:
        lista_notas.append(nota)
        contador_notas+=1
    else:
        print('Coleta de notas encerrada')
        break

def calcular_media(notas):
    media=sum(notas)/contador_notas
    print(f'Com base em suas {contador_notas} notas sua média é de {media:.2f}')

def verificar_situacao(notas):
    media=sum(notas)/contador_notas
    if media <7:
        print('Reprovado')
    elif 7<=media<10:
        print('Aprovado')
    else:
        print('Parabéns, sua média é 10!')


calcular_media(lista_notas)
verificar_situacao(lista_notas)
