# Métodos de listas
lista  = [1, 3, 12, 8, 2]

#append - Adiciona um elemento no final da lista
print('Lista antes:', lista)
lista.append(3)
print('Lista depois:', lista)

# insert -  escolho onde colocar o elemento
           # (index, elemento para adicionar)
lista.insert(2, 10)
print('Lista depois:', lista)

# extend - junta duas listas
lista2 = [1, 2, 3]

lista.extend(lista2)
print('Lista depois:', lista)

# pop -  remove o ultimo elemento elemento ou o que eu especificar

lista.pop()
print('Lista depois de pop:', lista)

lista.pop(0)
print('Lista depois pop com parametro:', lista)

#remove - indico o elemento que quero remover - remove o primeiro elemento que encontra

lista.remove(3)
print('Lista depois do remove:', lista)

#count - conta quando elementos especificos tem na lista

print("count:",lista.count(2))

# index -  retorna o index de um elemento

print('index:', lista.index(12))

#sort - ordena a lista
lista.sort() #ondem crescende
print('Sort:', lista)
lista.sort(reverse=True) #ondem decrescende
print('Sort rev:', lista)

#FUNÇÕES DE LISTA

# len - tamanho da lista
print('len:',len(lista))

# sum -  soma dos elementos da lista
print('sum:',sum(lista))

# max e min
print('Max:', max(lista))
print('Mim:', min(lista))
