#Crie um programa que vai gerar CINCO NÚMERO ALEATÓRIOS a colocar em uma TUPLA.
# Depois disso, mostre a LISTAGEM DE NÚMERO gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
a = sorted(tupla)
maior = menor = tupla[0]
print("Os valores sorteados foram: {}".format(tupla))

print("O menor valor é {}".format(sorted(tupla)[0]))
print("O maior valor é {}".format(sorted(tupla)[4]))

print("Também é possível encontrar os valores maior e menores com for tipo assim: ")

for c in tupla:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c

print(f"Menor: {menor}")
print(f"Maior: {maior}")

print("Também é possível fazer assim: ")
print("Maior: {}".format(max(tupla)))
print("Menor: {}".format(min(tupla)))