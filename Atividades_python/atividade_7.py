'''
7 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
lista = []
for cont in range(3):
    numero = int(input('Digite um numero inteiro: '))
    lista.append(numero)
lista.sort(reverse = True)
print(lista)