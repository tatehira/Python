'''
10- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
a temperatura em graus Celsius.
Obs: C = 5 * ((F-32) / 9).
'''
print('============================================ ')
print('CONVERSOR DE Fahrenheit, para graus Celsius! ')
print('============================================ ')
F = float(input('Digite o grau em Fahrenheit: '))
conversor = 5 * ((F-32) / 9)
print(f'O {F} convertido de Fahrenheit para Celsius é: {conversor:.2f}')