"""
Módulo random

Neste exercício pratiquei:
- geração de números aleatórios inteiros e decimais
- arredondamento e ajuste de intervalo
- escolha de elementos em lista (um ou vários)
- embaralhamento de lista (shuffle)
"""

import random

# Ex 1: gerar 5 números inteiros aleatórios entre 1 e 50
print('Gerar cinco números aleatórios entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1, 50)  # randint(a,b) inclui os extremos
    print(f'Número gerado: {n}')

# Ex 2: gerar número decimal aleatório entre 0 e 1 e multiplicar
valor = random.random()  # gera float entre 0 e 1
print(f'Número gerado: {round(valor * 10, 2)}')  # arredonda para 2 casas

# Ex 3: gerar número decimal aleatório entre 1 e 100
valor = random.uniform(1, 100)  # gera float entre 1 e 100
print(f'Número: {round(valor, 4)}')  # arredonda para 4 casas decimais

# Ex 4: escolher um elemento aleatório de uma lista
L = [1, 2, 3, 4, 5, 6, 7, 8]
n = random.choice(L)
print(f'Número escolhido: {n}')

# Ex 5: escolher vários elementos aleatórios da lista (sem repetição)
n = random.sample(L, 3)  # seleciona 3 elementos únicos
print(f'Números escolhidos: {n}')

# Ex 6: embaralhar a lista
print(f'Lista original: {L}')
random.shuffle(L)  # embaralha a lista **in-place**, não retorna valor
print(f'Lista embaralhada: {L}')

