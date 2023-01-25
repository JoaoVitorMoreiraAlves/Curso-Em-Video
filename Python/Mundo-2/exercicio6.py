#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 25 anos: SÊNIOR
#Acima: MASTER
from datetime import date
idade = int(input("Digite sua data de nascimento: "))

idade = date.today().year - idade

print("Idade: {}".format(idade))
if (idade <= 9):
    print("Classe Mirim")
elif (idade <= 14):
    print("Classe Infantil")
elif (idade <= 19):
    print("Classe Junior")
elif (idade <= 25):
    print("Classe Sênior")
else:
    print("Classe Master")