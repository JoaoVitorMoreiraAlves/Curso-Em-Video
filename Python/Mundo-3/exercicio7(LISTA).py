#Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
#No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas posições na lista.

num = []
maior = menor = 0
posicaomenor = posicaomaior = 0
for c in range(0,5):
    num.append(int(input(f"Digite um número na posição {c}: ")))

for cont,valor in enumerate(num):
    if cont == 0:
        maior = menor = valor
    if valor < menor:
        menor = valor
        posicaomenor = cont
    if valor > maior:
        maior = valor
        posicaomaior = cont

print("-="*30)
print("Você Digitou os valores {}".format(num))

print(f"O maior valor é {maior} e está nas posições ", end="")

for i,v in enumerate(num):
    if v == maior:
        print(f"{i} ",end="")
print("")

print(f"O menor valor é {menor} e está na posições ",end="")

for i,v in enumerate(num):
    if v == menor:
        print(f"{i} ", end="")