'''
25- Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e
gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

• O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
• O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''
#Lista de ips permitidos
ip_validos = open('ips_validos.txt','r') #arquivo criado previamente
lista_validos = ip_validos.readlines()

#Tratamento de dados da lista
for index in range(len(lista_validos)):
    
lista_validos[index] = lista_validos[index].rstrip('\n')

#Lista de ips a serem avaliados
ips_avaliar = open('ips_avaliar.txt','r') #arquivo criado previamente
lista_avaliar = ips_avaliar.readlines()

#Tratamento de dados da lista
for index in range(len(lista_avaliar)):
lista_avaliar[index] = lista_avaliar[index].rstrip('\n')

#Criando os arquivos onde serão gravados os dados de saida
logip_validos = open('logip_validos.txt','w+')
logip_invalidos = open('logip_invalidos.txt','w+')

#Cabeçalho dos arquivos de saida
logip_validos.write('[Endereços válidos:]\n')
logip_invalidos.write('[Endereços inválidos:]\n')

#Analise e gravação de dados
for ip in lista_avaliar:
if lista_validos.count(ip) == 0:
logip_invalidos.write(ip+'\n')
else:
logip_validos.write(ip+'\n')

logip_validos.close()
logip_invalidos.close()