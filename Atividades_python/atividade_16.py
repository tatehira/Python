'''
16- Desenvolva um jogo de acerte o número, onde o computador escolhe um número
inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número
'''
import random

sorteio = random.randint(0,10)
tentativas = 5
while True:
    chute = int(input('Digite um números positivo entre 0 e 10: '))
    if chute == sorteio:
            print(f'parabéns! Voce acertou. O número secreto é o {sorteio}')
            break
    else:
        if chute != sorteio:
            tentativas -= 1
            print(f'Voce errou! Ainda lhe falta {tentativas} tentativas! ')
        if tentativas == 0:
            print('Acabou todas as suas tentativas! Tente novamente mais tarde.')
            break