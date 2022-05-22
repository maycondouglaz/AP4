par_impar = input("******AP4 - LISTA COM PYTHON******")

i = 0
numeroMoradores = int(input("Número de moradores: "))
mediaConsumo = 0
energiasDosMoradores = []
quantidadeAcima = 0

while i < numeroMoradores :

    qtdEnergia = int(input("Quantidade de consumo de energia do primeiro morador: "))
    energiasDosMoradores.insert(i, qtdEnergia)
    i += 1

def mediaDosMoradores_E_moradoresAcimaDaMedia(energiasDosMoradores) :
    mediaConsumo = sum(energiasDosMoradores)/ len(energiasDosMoradores)
    print("Media de Consumo dos Moradores", mediaConsumo)
    quantidadeAcima = len([n for n in energiasDosMoradores if n > mediaConsumo])
    print("Quantidade de moradores que ficaram acima da média do consumo" , quantidadeAcima)

mediaDosMoradores_E_moradoresAcimaDaMedia(energiasDosMoradores)
print("----------------------------------------------------------")
print("fim")
