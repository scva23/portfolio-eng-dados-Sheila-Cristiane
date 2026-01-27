"""
While

Neste exercício, pratiquei:
- laço while (repete enquanto a condição for verdadeira)
- loop infinito com break para encerrar
- uso de continue para pular iterações
"""

# Ex 1: while com condição
num = 1
while num <= 10:       # repete enquanto num <= 10
    print(num)
    num += 1           # incrementa num
print("Laço encerrado.")

# Ex 2: while infinito com break e continue
while True:
    nome = input("Digite seu nome (ou 'x' para encerrar): ").strip()

    # se digitar 'x' → encerra o loop
    if nome.lower() == 'x':
        break

    # se não digitar nada → continua o loop (pula o print)
    if not nome:
        print("Você não digitou nada. Tente novamente.")
        continue

    # se digitou algo válido → imprime saudação
    print(f"Olá, {nome}!")

print("Até logo!")


              