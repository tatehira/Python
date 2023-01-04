'''
1 - Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a
média final, a maior nota e a menor nota
'''
notaaluno =[]
media = 0
maior_nota = 0
menor_nota = 0

print("Digite quatro notas: ")
for i in range(4):
    notaaluno.append(float(input("Nota" + str(i+1) + ":")))
    media += notaaluno[i]
    media = media/4
    if i == 0:
        maior_nota = menor_nota = notaaluno[i]
    else:
        if notaaluno[i] > maior_nota:
            maior_nota = notaaluno[i]
        if notaaluno[i] < menor_nota:
            menor_nota = notaaluno[i]

print(f"A média do aluno é: {round(media, 2)}")
print(f"A sua maior nota foi: {maior_nota}")
print(f"A sua menor nota foi: {menor_nota}")
