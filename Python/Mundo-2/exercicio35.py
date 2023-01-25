#Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de 1k
# C) Qual o nome do produto mais barato.

barato = 99999999999999999999999999999999999999999999
acima1k = total = 0
nomebarato = opinador = ""
while True:
    if opinador == "N":
        break
    nome = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o valor do produto: "))
    total += valor

    if valor > 1000:
        acima1k += 1
    if valor < barato:
        barato = valor
        nomebarato = nome
    opinador = ""
    
    if opinador != "S":
        while opinador != "S" and opinador != "N":
            opinador = str(input("Deseja continuar? [N/S]: ")).upper().strip()[0]
print("Total da compra {}".format(total))
print("Produtos acima de 1k : {}".format(acima1k))
print("Qual o nome do produto mais barato? {}".format(nomebarato))