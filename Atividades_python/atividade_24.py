'''
24- Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
não deve ser armazenado). Após esta entrada de dados, faça:

b. Mostre a quantidade de valores que foram lidos;
c. Exiba todos os valores na ordem em que foram informados, um ao lado do
outro;
d. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do
outro;
e. Calcule e mostre a soma dos valores;
f. Calcule e mostre a média dos valores;
g. Calcule e mostre a quantidade de valores acima da média calculada;
h. Calcule e mostre a quantidade de valores abaixo de sete;
i. Encerre o programa com uma mensagem;
'''

lista_valor = []
soma_valores = 0
valor = 0
abaixo_de_7 = 0
acimamedia = 0
reverse = 0
mean = 0

vezes = int(input('Digite quantos numeros deseja colocar: '))

for cont in range(vezes):
    valor = float(int(input('Digite um valor: ')))
    lista_valor.append(valor)

    soma_valores = sum(lista_valor)
    quantidade = len(lista_valor)

    import statistics
    mean = statistics.mean(lista_valor)

    if valor > mean:
        acimamedia += 1
    if valor <= 7:
        abaixo_de_7 += 1
    if valor <= -1:
        break

reversa = lista_valor[::-1]

print(f'A quantidade total de valores digitado é: {quantidade}')
print(f'Os valores na ordem inversa do digitado, um abaixo do outro: {reversa}')
print(f'Os valores digitados: {lista_valor}')
print(f'A soma dos valores: {soma_valores}')
print(f'A média dos valores é: {mean:.2f}')
print(f'A quantidade de valores acima da média: {acimamedia}')
print(f'A quantidade de valores abaixo de sete: {abaixo_de_7}')