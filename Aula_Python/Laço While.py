numero_sorteado = 15

numero_escolhido = int(input("Escolha um número entre 1 e 20: "))

while(numero_escolhido!=numero_sorteado):
    print("ERRROUUU! \nTente novamente")
    numero_escolhido = int(input("Escolha um número entre 1 e 20: "))

print("ACERTOUUU!!!")


#EX2: Estrutura com contador

contador = 0

while(contador<5):
    print(contador)

    contador = contador + 1
