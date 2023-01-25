#Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 99999
for i in range(1,6):
    peso = float(input("Digite o peso da {}º pessoa: ".format(i)))
    if (peso > maior):
        maior = peso
    if (peso < menor):
        menor = peso
print("O maior peso foi {}\nO menor peso foi {}".format(maior,menor))