''' Faça um programa que leia a quantidade de pessoas que serão 
convidadas para uma festa. Após isso, o programa irá perguntar 
o nome de todas as pessoas e colocar uma lista de convidados. 
Após isso, irá imprimir todos os nomes da lista.'''
quant = int(input("Quantas pessoas serão convidadas para a a festa?\n"))
num = 0
convidados = []
print("Quem vai a festa?")
while num < quant:
    conv = input("-> ")
    convidados.append(conv)
    num += 1
print(f'vão na pizza: {convidados}\nou seja, só os chegados...')