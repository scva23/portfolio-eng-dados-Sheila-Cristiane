"""
Laços Encadeados

Aqui pratiquei:
- um laço dentro do outro para criar repetições em níveis
- o laço externo controla as rodadas/conjuntos
- o laço interno executa ações dentro de cada rodada
  (contagem regressiva ou geração de números aleatórios)
"""

# Ex 1: contagem regressiva dentro de rodadas
for cont_ex in range(1, 6):  # laço externo: 5 rodadas
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5, 0, -1):  # laço interno: contagem de 5 até 1
        print(f'Valor: {cont_in}')
print('Fim dos laços\n')

# Ex 2: gerar números aleatórios dentro de conjuntos
import random

for A in range(1, 6):  # laço externo: 5 conjuntos
    print(f'Conjunto {A}')
    for B in range(5):  # laço interno: gera 5 números aleatórios
        num = random.randint(1, 100)
        print(f'Valor: {num}')


