import sys # permite a utilização de alguns métodos do sistema operacional
argumentos = sys.argv

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

if argumentos[1] == "soma":
    resposta = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resposta = sub(float(argumentos[2]), float(argumentos[3]))
print(resposta)