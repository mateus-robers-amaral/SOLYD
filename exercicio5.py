# arquivo = open('arquivo.txt', 'w') # arquivos de texto: r, w, a | arquivos exe, imagens: b

#  for i in range(0, 1001):
#      arquivo.write("coe" + str(i) + "\n")

arquivo = open('bigas.jpeg', 'rb')
print(arquivo.read())