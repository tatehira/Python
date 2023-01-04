'''
15- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total.
'''
print('============================')
print('Calculo para loja de tintas!')
print('Lata de tinta: 18 litros    ')
print('1 litro pinta 3 m²          ')
print('Valor da tinha: 80 R$       ')
print('============================')
cobertura = 3
volume = 18
valor_lata = 80
m_quadrado = float(input('Digite os metros quadrados que será pintado: '))
litros_que_usara = (m_quadrado/cobertura)
quant_latas = float(litros_que_usara/volume)

if (litros_que_usara % volume != 0):
    quant_latas += 1

total = (quant_latas * valor_lata)
print(f'Quantidade de litros: {litros_que_usara:.2f}')
print(f'Quantidade de latas de tintas: {int(quant_latas)}')
print(f'valor total: {total:.2f}R$')