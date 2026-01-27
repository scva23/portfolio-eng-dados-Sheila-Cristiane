"""
For, range e continue

Aqui pratiquei:
- iterar sobre listas e strings com for
- usar range() para gerar sequências numéricas
- usar continue para pular um item específico
"""

# Ex 1: iterando sobre uma lista
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(f"Item da lista: {item}")

# Ex 2: iterando sobre uma string
palavra = "Python"
for letra in palavra:
    print(f"Letra: {letra}")

# Ex 3: range simples
for numero in range(1, 11):  # de 1 até 10
    print(f"Número atual: {numero}")

# Ex 4: range com input do usuário
nome = input('Digite seu nome: ')
for x in range(10):
    print(f"{x+1} - Olá, {nome}!")

# Ex 5: range com passo positivo e negativo
for x in range(2, 20, 2):  # de 2 até 18, de 2 em 2
    print(x)

for x in range(5, 0, -1):  # de 5 até 1, decrementando
    print(x)

# Ex 6: continue para pular elementos
pedras = ("ametista", "quartzo rosa", "jade", "turmalina", "ágata")
for pedra in pedras:
    if pedra == "quartzo rosa":
        continue  # pula essa iteração
    print(pedra)
