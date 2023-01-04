'''
6 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
calcular a média alcançada por aluno e apresentar:
a. A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
b. A mensagem "Reprovado", se a média for menor do que 7;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7 and media <= 9:
    print(f'A sua média foi {media} e voce está Aprovado! ')
elif media < 7:
    print(f'A sua média foi {media} e voce está Reprovado! ')
elif media == 10:
    print(f'A sua média foi {media} e voce está Aprovado com distrição! ')
else:
    print('Parabens')