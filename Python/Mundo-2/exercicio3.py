#Escreva um programa que leia dois número inteiro e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if (num1 > num2):
    print("O PRIEMIRO NÚMERO É MAIOR, pois o número {} é maior que o número {}".format(num1,num2))
elif (num2 > num1):
    print("O SEGUNDO NÚMERO É MAIOR, pois o número {} é maior que o número {}".format(num2,num1))
else:
    print("Os número {} e {} são iguais".format(num1,num2))