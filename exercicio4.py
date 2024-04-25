''' Escreva uma função que recebe um objeto de coleção e retorna
o valor do maior número dentro dessa coleção e faça outra função 
que retorna o menor número dessa coleção '''
coletar = int(input("Digite quantos membros você deseja por na coleção: \n"))
num = 0
colecao = []
loop = print("Digite o(s) número(s) que deseja incluir.")
while num < coletar:
    loop1 = float(input("-> "))
    colecao.append(coletar)
    num += 1

def maior():
    big = 0
    for item in colecao:
        if item > big:
            big = item
    print(f"O maior número é {big}")

def menor():
    les = 10000000000000000000000000000
    for item in colecao:
        if item < les:
            les = item
    print(f"O menor número é {les}")

maior()
menor()