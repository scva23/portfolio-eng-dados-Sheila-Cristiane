"""
Operadores Lógicos (and, or, not)

Neste exercício, praticamos como combinar condições booleanas para tomar decisões.
- AND: exige que **todas** as condições sejam verdadeiras
- OR: aceita que **uma ou mais** condições sejam verdadeiras
- NOT: inverte o valor booleano
"""

# Ex 1: Verificação de idade e altura
idade = 19
altura = 1.75

# AND → precisa que as duas condições sejam verdadeiras
resultado = idade >= 18 and altura >= 1.70
print("A pessoa é maior de idade e tem altura suficiente:", resultado)

# OR → basta que uma condição seja verdadeira
resultado = idade < 18 or altura < 1.70
print("A pessoa é menor de idade ou tem altura insuficiente:", resultado)

# Ex 2: Programa de disparo de alarme
porta = 'f'   # 'a' = aberta
janela = 'a'  # 'a' = aberta

# Se porta ou janela estiver aberta → disparar alarme
alarme = (porta == 'a' or janela == 'a')
print("Disparar alarme:", alarme)

# Ex 3: Programa de compra usando NOT
tem_dinheiro = False

# NOT inverte o valor
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro para comprar? ' + str(tem_dinheiro)
print(msg)

