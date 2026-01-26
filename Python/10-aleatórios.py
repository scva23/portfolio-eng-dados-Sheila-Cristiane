
"""
Módulo random

Neste exercício pratiquei:
- geração de números aleatórios inteiros e decimais
- arredondamento e ajuste de intervalo
- escolha de elementos em lista (um ou vários)
- embaralhamento de lista (shuffle)
"""


import random

#Ex 1:
print('Gerar cinco números aleatórios entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')

#Ex 2:
valor = random.random()
print(f'Numero gerado: {round(valor * 10, 2)}')

#Ex 3:
valor = random.uniform(1,100)
print(f'Número: {round(valor,4)}')

#Ex 4:
L = [1,2,3,4,5,6,7,8]
n = random.choice(L)
print(f'Número escolhido: {n}')

#Ex 5:
n = random.sample(L, 3)
print(f'Números escolhidos {n}')

#Ex 6:Embaralhar
print(f'Exibir lista original: {L}')
print(f'Embaralhar a lista e exibí-la:')
n = random.shuffle(L)
print(L)

