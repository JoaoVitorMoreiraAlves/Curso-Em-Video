#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa, mostra:
# A média de idade do grupo.
# qual é o nome do homem mais velho.
# quantas mulheres tem menos de 20 anos.
media = 0
maior = 0
velho = ""
mulheres = 0
for i in range(1,5):
    nome = str(input("Digite o nome da {} º pessoa: ".format(i)))
    idade = int(input("Digite a idade da {}º pessoa: ".format(i)))
    sexo = int(input("Digite 1 para Homem e 2 para mulher da {}º pessoa: ".format(i)))
    media += idade
    if (sexo == 1 and idade > maior):
        maior = idade
        velho = nome
    if (sexo == 2 and idade < 20):
        mulheres += 1
print("A média das idade é de {}".format(media/4))
print("O nome do HOMEM mais velho é {}".format(velho))
print("Teve {} mulheres abaixo de 20 anos".format(mulheres))