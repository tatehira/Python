'''
17- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
try:
    while True:
        nota = int(input('Digite uma nota entre 0 e 10! '))
        if nota >= 0 and nota <= 10:
            print('Nota validada. Obrigado! ')
            break
        elif nota < 0 or nota > 10:
            print('Erro! Somente é valido notas entre 0 e 10. Tente novamente! ')
            continue
except ValueError:
    print('Caractere inválido! Tente novamente.')
