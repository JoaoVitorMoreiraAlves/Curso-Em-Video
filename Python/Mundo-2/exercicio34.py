#Crie um programa que leia a IDADE e o SEXO de VARIAS PESSOAS. A cada pessoa cadastrada, o programa deverá perguntar se o USUÁRIO quer ou não continuar. No final, mostrar:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos Homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

idademaior = homens = mulher = 0

while True:
    idade = int(input("Digite a idade: "))

    sexo = str(input("Digite o Sexo [M/F]: ")).upper()[0]
    while sexo not in 'MF':
        sexo = str(input("Digite o Sexo [M/F]: ")).upper()[0]
    if idade > 18:
        idademaior += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and  idade < 20:
        mulher += 1
    
    opinador = str(input("Deseja continuar ou não? [N/S]: ")).upper().strip()[0]
    while opinador not in 'SN':
        opinador = str(input("Deseja continuar ou não? [N/S]: ")).upper().strip()[0]

    if opinador == "N":
        break
print("A quantidade de pessoas maiores de 18 anos é de {}".format(idademaior))
print("A quantidade de Homens foi de {}".format(homens))
print("A quantidade de mulheres abaixo de 20 anos foi de {}".format(mulher))