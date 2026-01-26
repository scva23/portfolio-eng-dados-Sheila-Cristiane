
"""
Print e Formatação

Aqui eu estudei maneiras diferentes de imprimir mensagens:
- print com vírgulas
- concatenação de strings
- format()
- f-strings
- end=' ' para manter na mesma linha
- formatação de casas decimais e tabulação
"""

mensagem = 'Função print em Python'
print(mensagem)
print("Aula de python")

nome = 'Sheila'
print("Olá,", nome)

nome = input("Digite seu nome: ")
print("Olá " + nome + ", seja bem-vindo(a)!")

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem sem mudar de linha', end=' ')
print('Continuação da mensagem na mesma linha')

a = 10
b = 5
res = f'A soma de {a} + {b} é igual a {a + b}'
print(res)

valor = 125.795585
print(f'O valor é {valor:.2f}')  # 2 casas decimais

print(f"O valor é '{valor:.2f}'")  # aspas dentro do texto

nome = 'Sheila Cristiane'
idade = 19
print(f'Nome: {nome}\tIdade: {idade}')  # tabulação com \t
