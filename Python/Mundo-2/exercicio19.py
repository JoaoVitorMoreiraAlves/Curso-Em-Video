#Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não antigiram a maioridade e quantias ja são maiores.
from datetime import date
maior = 0 
menor = 0
for i in range(1,8):
    num = int(input("Digite a data de nascimento da {}º pessoa: ".format(i)))
    if ((date.today().year - num) >= 21):
        maior += 1
    else:
        menor += 1
print("A quantidade de pessoas maior de idade são {} e as menores de idade são {}".format(maior,menor))