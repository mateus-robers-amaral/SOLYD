''' Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decide se ela está apta a ser do exército. Para entrar no exército é preciso
ter mais de 18 anos, pesar mais ou igual 60 kilos
e medir mais ou igual 1,70 metros'''
age = int(input("Qual a sua idade? "))
weight = int(input("Qual o seu peso? "))
high = float(input("Qual a sua altura? "))

if age >= 18 and weight >= 60 and high >= 1.70:
    print("Você está apto a servir.")
else:
    print("Você não está apto a servir, dispensado.")
