'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-
matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa

Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
horario = int(input('Se voce estuda no periodo: \n-MATUTINO, digite: ---[1] \n-VESPERTINO, digite: -[2] \n-NOTURNO, digite: ----[3]'))

if horario == 1:
    print('Bom dia! ')
elif horario == 2:
    print('Boa tarde! ')
elif horario == 3:
    print('Boa noite! ')
else:
    print('Valor inválido! Revise os números.')