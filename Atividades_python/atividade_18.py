'''
18- Faça um programa que leia 5 números e informe o maior número.
'''
print('programa que diz qual dos 5 numeros ditados é o maior! ')
lista = []
maior = 0
i = 1
for i in range(5):
    lista.append(int(input('Digite um número: ')))
    max = float('-inf')
    for maior in lista:
        maior = int(maior)
        if maior > max:
            max = maior
print(f'O maior numero da lista é o {max}')