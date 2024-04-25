def soma(num1, num2):
    res = num1 + num2
    return res
retorno = soma(75, 1259)
print(retorno)

def imprime_oi():
    print("oi ^^")
imprime_oi()

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
if tem_sete_itens('1234567'):
    print("Realmente tem sete números!")