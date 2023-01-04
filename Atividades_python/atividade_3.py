'''
3- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota >= 0 and nota <= 10:
        print('Você digitou o valor entre 0 e 10! Parabens.')
    elif nota < 0 or nota > 10:
        print('Somente números entre 1 e 10: ')
    else:
        break
