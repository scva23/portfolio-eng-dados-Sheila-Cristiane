"""
Variáveis e Tipos

Neste exercício, pratiquei:
- criação de variáveis
- tipos básicos
- verificação do tipo com type()
- checagem de tipo com isinstance()
"""

# Ex 1: criação de variáveis
media = 0                     # int
n1 = n2 = n3 = n4 = 0.5      # float
nome, idade = 'Sheila', 30    # string e int
estado = True                  # bool
a = 10                         # int
b = 'sol'                      # string

# Ex 2: verificando o tipo das variáveis com type()
print(type(media))  # <class 'int'>
print(type(nome))   # <class 'str'>
print(type(n1))     # <class 'float'>
print(type(estado)) # <class 'bool'>

# Ex 3: checando o tipo com isinstance()
print(isinstance(idade, int))   # True
print(isinstance(nome, str))    # True
print(isinstance(a, str))       # False
