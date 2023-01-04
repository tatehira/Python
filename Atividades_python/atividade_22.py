'''
22- Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
ordem lida.
'''
lista_idade = []
lista_altura = []

for i in range(5):
    idade = int(input(f'Digite a {i+1} idade: '))
    lista_idade.append(idade)
    altura = float(input(f'Digite a {i+1} altura: '))
    lista_altura.append(altura)
    print('========================')

lista_idade = sorted(lista_idade, key= int, reverse=True)
lista_altura = sorted(lista_altura, key= float, reverse=True)
print(f'As idades digitadas de forma reversa: {lista_idade}')
print(f'As alturas digitadas de forma reversa: {lista_altura}')