"""
Condicionais (if / elif / else)

Neste exercício, calculei a média de duas notas e classifiquei o resultado:
- Aprovado (>= 7)
- Recuperação (>= 5 e < 7)
- Reprovado (< 5)
"""

# Entrada das notas
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

# Cálculo da média
media = (n1 + n2) / 2

# Classificação usando if / elif / else
if media >= 7:
    print("Resultado: Aprovado")
elif media >= 5:  # se media >= 5 e < 7
    print("Resultado: Recuperação")
else:
    print("Resultado: Reprovado")

# Exibindo a média
print("Sua média é {:.2f}".format(media))
