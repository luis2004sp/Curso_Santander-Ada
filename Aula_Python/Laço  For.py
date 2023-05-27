"""for i in range(0,5):
    print(i+1)"""


"""for i in range(1, 10):
    print(i)"""

"""for i in range(0, 1001, 5):
    print(i)"""



# exec
soma = 0
for i in range(0, 3):
    nota = float(input(f"Digite sua nota {i+1}: "))
    soma = soma + nota


print(f"Média = {soma/3}")