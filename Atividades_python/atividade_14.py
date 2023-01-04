'''
14- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
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
    IR = ((11/100)*calculo)
    INSS = ((8/100)*calculo)
    sindicato = ((5/100)*calculo)
    desconto = (IR+INSS+sindicato)
    print(f'Você tem o salario de {calculo} por mês! ')
    print(f'O valor descontado do Imposto: {IR}')
    print(f'O valor descontado de INSS: {INSS}')
    print(f'O valor descontado de Sindicato: {sindicato}')
    print(f'O valor total de desonto é: {desconto}')
elif semanais == 'b':
    calculo2 = float((sabado  * horas_trabalhadas) * 4)
    calculo += calculo2
    IR = ((11/100)*calculo)
    INSS = ((8/100)*calculo)
    sindicato = ((5/100)*calculo)
    desconto = (IR+INSS+sindicato)
    print(f'Você tem o salario de {calculo} por mês! ')
    print(f'O valor descontado do Imposto: {IR}')
    print(f'O valor descontado de INSS: {INSS}')
    print(f'O valor descontado de Sindicato: {sindicato}')
    print(f'O valor total de desonto é: {desconto:.2f}')
else:
    print('parametro inválido! ')
