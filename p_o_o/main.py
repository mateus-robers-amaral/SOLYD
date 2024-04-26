from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo("rosa", "volvo", 8, 10)
carro_azul = Carro("azul", "Toyota", 8)

print(f'Cor: {caminhao_rosa.cor}; Marca: {caminhao_rosa.marca}; Rodas: {caminhao_rosa.rodas}; Tanque: {caminhao_rosa.tanque}')
print()
print(f'Cor: {carro_azul.cor}; Marca: {carro_azul.marca}; Rodas: {carro_azul.rodas}; Tanque: {carro_azul.tanque}')
carro_azul.abastecer(30)
print(carro_azul.tanque)
