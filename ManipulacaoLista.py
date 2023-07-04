# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Imprimindo a lista original
print("Lista original:", numeros)

# Acessando um elemento da lista pelo índice
primeiro_numero = numeros[0]
print("Primeiro número:", primeiro_numero)

# Modificando um elemento da lista
numeros[2] = 10
print("Lista modificada:", numeros)

# Adicionando um elemento no final da lista
numeros.append(6)
print("Lista após adição:", numeros)

# Removendo um elemento da lista
numeros.remove(4)
print("Lista após remoção:", numeros)

# Obtendo o tamanho da lista
tamanho = len(numeros)
print("Tamanho da lista:", tamanho)

# Verificando se um número está na lista
if 3 in numeros:
    print("O número 3 está na lista")
else:
    print("O número 3 não está na lista")

# Ordenando a lista em ordem crescente
numeros.sort()
print("Lista ordenada:", numeros)

# Invertendo a ordem dos elementos na lista
numeros.reverse()
print("Lista invertida:", numeros)
