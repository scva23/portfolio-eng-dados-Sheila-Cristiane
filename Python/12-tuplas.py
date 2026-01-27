# Tuplas parecem listas, mas são imutáveis (não podem ser alteradas após criadas)

# Ex 1: criando uma tupla simples
tupla = (2, 4, 6, 8)
print(tupla)

# Ex 2: tuplas com elementos químicos
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(halogenios[-2:])  # últimos dois elementos da tupla

gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres  # concatenar tuplas
print(elementos)

# Ex 3: métodos que tuplas têm
t1 = (1,1,2,2,3,3,4,4,5,5,6,6,1,2,3,6,5,4)
print(t1.count(3))  # conta quantas vezes o 3 aparece
print(sum(t1))      # soma todos os elementos

# Operações não disponíveis em tuplas (porque são imutáveis):
# .sort(), .append(), .reverse(), .pop() - essas só funcionam com listas

# Ex 5: percorrendo tuplas com for
for elemento in elementos:
    print(f'Elemento químico: {elemento}')

# Ex 7: converter tupla para lista para poder modificar
grupo17 = list(halogenios)
grupo17[0] = 'H'  # agora pode modificar
print(grupo17)

# Ex 8: criar tupla vazia
grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple()  # tupla vazia
print(type(alcalinos))  # confirma que é uma tupla
