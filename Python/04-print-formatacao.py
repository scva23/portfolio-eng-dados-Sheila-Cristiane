"""
Print e Formatação

Aqui estudei maneiras diferentes de imprimir mensagens em Python:
- print com vírgulas
- concatenação de strings
- format()
- f-strings
- end=' ' para continuar na mesma linha
- formatação de casas decimais e tabulação
"""

# Ex 1: print simples
mensagem = 'Função print em Python'
print(mensagem)
print("Aula de Python")

# Ex 2: print com vírgula (concatena com espaço)
nome = 'Sheila'
print("Olá,", nome)

# Ex 3: concatenação com + e input do usuário
nome = input("Digite seu nome: ")
print("Olá " + nome + ", seja bem-vindo(a)!")

# Ex 4: print com end=' ' para manter na mesma linha
print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem sem mudar de linha', end=' ')
print('Continuação da mensagem na mesma linha')

# Ex 5: f-strings
a = 10
b = 5
res = f'A soma de {a} + {b} é igual a {a + b}'
print(res)

# Ex 6: formatação de casas decimais
valor = 125.795585
print(f'O valor é {valor:.2f}')           # 2 casas decimais
print(f"O valor é '{valor:.2f}'")         # com aspas dentro do texto

# Ex 7: tabulação
nome = 'Sheila Cristiane'
idade = 19
print(f'Nome: {nome}\tIdade: {idade}')    # \t para tabulação

