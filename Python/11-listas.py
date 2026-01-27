# Listas são o tipo de sequência mais comum
# Representam uma sequência de valores
# Sintaxe: nome_lista = [valores]
# Índice começa em 0

# Ex 1: criar uma lista e imprimir
notas = [5, 7, 8, 9, 6]
print(notas)

# Ex 2: concatenar listas
n1 = [1, 2, 3, 4]
n2 = [5, 6, 7, 8]
valores = n1 + n2
print(valores)

# Acessando elementos negativos (conta de trás para frente)
print(valores[-2])

# Ex 3: alterar valores
valores[0] = 8
print(valores)

# Ex 4: slice (fatiamento)
# Mostra valores do índice 1 até 2 (o final não é incluído)
print(valores[1:3])

# Ex 5: contar elementos
print(len(valores))

# Ex 6: ordenação, soma, máximo e mínimo
print(sorted(valores))               # ordem crescente
print(sorted(valores, reverse=True)) # ordem decrescente
print(sum(valores))                   # soma dos elementos
print(max(valores))                   # maior valor
print(min(valores))                   # menor valor

# Ex 7: acrescentar elementos
valores.append(20)           # adiciona no final
print(valores)

valores.insert(3, 22)        # insere na posição 3, sem substituir
print(valores)

# Ex 8: remover elementos
valores.pop()                # remove o último elemento
print(valores)

valores.pop(3)               # remove o elemento na posição 3
print(valores)

# Ex 9: verificar se um valor está na lista
print(17 in valores)         # retorna True ou False

# Ex 10: laço for em listas
lista = [2, 6, 9, 4, 0, 12, 3, 7]
for item in lista:
    print(item)

# Ex 11: iteração sobre strings
palavra = 'sheila'
for letra in palavra:
    print(letra)

#Ex 12:
planetas = ['Mercurio', 'Vênus', 'Marte', 'Saturno']
for planeta in planetas:
    print(planeta)


#Ex: Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.

#Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repetição for.

bebidas = []

for i in range(5):
    bebida = input(f'Digite o nome da bebida favorita {i+1}: ')
    bebidas.append(bebida)

# Ordena a lista em ordem alfabética
bebidas_ordenadas = sorted(bebidas)

print("\nSuas bebidas favoritas em ordem alfabética:")
for bebida in bebidas_ordenadas:
    print(bebida)


