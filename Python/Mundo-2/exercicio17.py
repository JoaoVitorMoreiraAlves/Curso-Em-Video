#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite o valor: "))
tot = 0
for i in range(1,num+1):
    if (num % i == 0):
        print("\033[33m", end="")
        tot += 1
    else:
        print("\033[31m", end="")
    print("{} \033[m".format(i), end="")
print("\nO número {} foi divido ao todo {} vezes".format(num,tot))
if tot == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele não é primo")