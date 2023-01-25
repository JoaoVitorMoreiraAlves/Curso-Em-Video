#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o seu Sexo [M/F]: ")).upper().strip()[0]

while sexo != "M" and sexo != "F":
    sexo = str(input("Sexo errado por favor informe um Sexo entre M ou F: ")).upper().strip()[0]
print("Seu sexo é {}".format(sexo))