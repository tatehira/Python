'''
21- Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.
'''
from string import ascii_letters
qunt_str = int(input('Digite a quantidade de caracteres desejada: '))
lista = []

for i in range(0,qunt_str):
    caracteres = str(input(f'Digite o {i+1} caractere: '))
    lista.append(caracteres)
print(f'Lista de caracteres: {lista}')

def conta_consoante(caracteres):
    consoantes = set(ascii_letters) -set ('aeiouAEIOU')
    soma = 0
    for i in caracteres:
        if i in consoantes:
            soma += 1
    print(f'A quantidade de consoantes digitada é: {soma}')
    return soma
conta_consoante(lista)