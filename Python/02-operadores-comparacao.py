"""
Operadores de Comparação

Neste exercício pratiquei:
- comparação entre dois números
- uso dos operadores ==, > e !=
- atribuição de valores booleanos (True ou False)
- leitura de dados do usuário com input
"""


# Ex 1: Operadores de comparação

x = y = z = False
n1 = n2 = 0

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

# Igualdade
x = n1 == n2
print("São iguais?", x, '\n')

# Maior que
z = n1 > n2
print(n1, "é maior que", n2, "?", z, '\n')

# Diferente
y = n1 != n2
print("São diferentes?", y)

