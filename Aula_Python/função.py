#Função inicial

def saudacao():
    print("Ola usuario!")

saudacao()

#função com parâmetro
def saudacao(s , curso):
    print(f"Ola {s}!")
    print(f'Tenha um bom curso de {curso}')

s = 'Luis'
curso = "Banco de Dados"
saudacao(s, curso)

#função com parâmetro default
def saudacao(s , curso='python'):
    print(f"Ola {s}!")
    print(f'Tenha um bom curso de {curso}')

s = 'Luis'
saudacao(s)

#Funções com retorno
def soma(n1, n2):
    return n1+n2

print(soma(7, 4))

def calculadora(n1, n2, operacao = '+' ):
    if (operacao == '+'):
        return n1+n1
    elif(operacao == '-'):
        return n1-n2
    elif(operacao=='*'):
        return n1*n2
    elif (operacao == '/'):
        return n1/n2
    
print(calculadora(2, 3))
print(calculadora(2, 3, '-'))
print(calculadora(2, 3, '*'))
print(calculadora(2, 3, '/'))
