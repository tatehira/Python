'''
9 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''
calculo = 0
calculo2 = 0
valor_hora = float(input('Voce ganha quantos por HORAS TRABALHADAS? '))
horas_trabalhadas = float(input('Quantas horas você trabalha por dia? '))
semanais = (input('Pressione: [A] Se você trabalha de segunda-a-sexta ou [B] se for de segunda-a-sabado? '))
if semanais == 'a':
    pass
elif semanais == 'b':
    sabado = float(input('Você trabalha quantas horas no sabado? '))
else:
    print('Fim da execução! ')

calculo = float((valor_hora * horas_trabalhadas) * 22)

if semanais == 'a':
    print(f'Você tem o salario de {calculo} por mês! ')
elif semanais == 'b':
    calculo2 = float((sabado  * horas_trabalhadas) * 4)
    calculo += calculo2
    print(f'Você trabalha {calculo}')
else:
    print('parametro inválido! ')
