# sem lista :(
n1 =10
n2 = 5
n3 = 4

# com listas :)
notas = [10, 5, 4]

# criação de lista
lista = []
lista = list() 

lista = [ 20, 'luis', 3.14,  True]

matriz = [20, ['luis']]


# Slice

lista = [10,20,30,40,50,60]

print(lista[0:3]) #imprime de 0 até o indice 2
print(lista[0 : len(lista) : 2])

# usando o  for in

for elemento in lista:
    print(elemento)

print('----------------------')
# usando comprimento
for i in range(len(lista)):
    print(lista[i])