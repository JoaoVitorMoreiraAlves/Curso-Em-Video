#Crie um programa que leia um número qualquer inteiro e mostre na tela se ele é PAR ou Impar.

num = int(input("Digite o número de consulta: "))


if num % 2 != 0:
    print("O número {} é impar".format(num))
else:
    print("O número {} é par".format(num))