'''
19-O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1.99, com cerca de 10
caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma
tabela que contém o número de itens que o cliente comprou e ao lado o valor da
conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente
está levando e olhar na tabela de preços. Você foi contratado para desenvolver o
programa que monta esta tabela de preços, que conterá os preços de 1 até 50
'''
print('Tabela de preços! ')
valor = 1.99
unidade = 1
calculo = 1.99
while True:
    print(f'O valor de {unidade} unidade(s) é: {calculo:.2f}R$')
    calculo += valor
    unidade += 1
    if unidade == 50:
        print('fim da execução! ')
        break
