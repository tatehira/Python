'''
20- Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será
digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e
terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
conforme exemplo abaixo:
• Montar a tabuada de: 5
• Começar por: 4
• Terminar em: 7
•
• Vou montar a tabuada de 5 começando em 4 e terminando em 7:
• 5 X 4 = 20
• 5 X 5 = 25
• 5 X 6 = 30
• 5 X 7 = 35
'''
try:
    tabuada = int(input('Qual tabuada gostaria de ver? '))
    comeco = int(input('Começa de: '))
    final = int(input('Termina em: '))
    cont = comeco
    if comeco > final:
        print('O valor inicial não pode ser maior que o final! ')
        exit()
    while True:
        calculo = tabuada * cont
        print(f'{tabuada} x {cont} = {calculo}')
        cont += 1
        if cont == final:
            break
except ValueError:
    print('Caractere inválido. tente novamente! ')