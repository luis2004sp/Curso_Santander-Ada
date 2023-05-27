# Criando dicionario
dicionario = {}
dicionario = dict()

dicionario = {'nome':'Luis', 'idade': 26, 'altura':1.8 }

print(dicionario)

print(dicionario['idade'])

#adicionando ao dicionario
dicionario['programador']= True
print(dicionario)

#iteração

for chave in dicionario:
    print(chave,dicionario[chave])

#Vendo se ja existe a chave no dicionario
print(not 'peso' in dicionario)
print('altura' in dicionario)
