'''
13- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se
o mesmo é: equilátero, isósceles ou escaleno.
-------------------------------------------------------------------------
a. Três lados formam um triângulo quando a soma de quaisquer dois lados for
maior que o terceiro;
b. Triângulo Equilátero: três lados iguais;
c. Triângulo Isósceles: quaisquer dois lados iguais;
d. Triângulo Escaleno: três lados diferentes;
'''
lado1 = int(input('Digite o primeiro lado do triangulo: '))
lado2 = int(input('Digite o segundo lado do triangulo:  '))
lado3 = int(input('Digite o terceiro lado do triangulo: '))

if lado1 == lado2 and lado2 == lado3:
    print('Este é um triangulo Equilátero! ')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Este é um triangulo Isósceles! ')
elif lado1 != lado2 and lado2 != lado3:
    print('Este é um triangulo Escaleno! ')
else:
    print('Revise o o numero digitado! Parametro inválido.')