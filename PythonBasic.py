# Declaração de variáveis e tipos de dados

# Variáveis numéricas
idade = 25
altura = 1.75
salario = 2500.50

# Variáveis de texto (string)
nome = "João"
sobrenome = 'Silva'

# Variável booleana
ativo = True

# Operações matemáticas básicas

# Soma
resultado = 10 + 5

# Subtração
resultado = 20 - 8

# Multiplicação
resultado = 6 * 4

# Divisão
resultado = 15 / 3

# Exponenciação
resultado = 2 ** 3

# Módulo (resto da divisão)
resultado = 20 % 7

# Estruturas de controle

# Condicionais (if-else)

# Verifica se um número é positivo, negativo ou zero
num = -5
if num > 0:
    print("O número é positivo")
elif num < 0:
    print("O número é negativo")
else:
    print("O número é zero")

# Laços de repetição (while e for)

# Loop while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Loop for
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print("Fruta:", fruta)

# Funções

# Declaração de uma função simples
def somar(a, b):
    return a + b

# Chamada da função
resultado = somar(3, 4)
print("Resultado:", resultado)
