#Conhecendo as variáveis
'''
    Sou um comentario de varias linhas
'''
"""
    Comentario de varias linhas
"""
texto = "2" #variavel do tipo string
texto1 = str(2) #variavel do tipo string
numero = 3  #variravel do  tipo numérico
numero1 = int(3) #variavel do tipo inteiro
numero2 = float(3.2) #variavel do tipo real

print(texto)
print(numero2)

#entrada de dados
nome = input('Digite o nome: ')
print('Olá', nome , '!')
num1 = int(input('{} Digite sua idade: '.format(nome)))
print(f'Ola {nome}, sua idade {num1}')

altura = float(input(f'{nome} digite sua altura: '))
print(f'Ola {nome} sua idade {num1} e sua altura{altura:.2f}')