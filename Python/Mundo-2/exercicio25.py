#Faça um programa que leia um número qualquer e mostre o seu fatorial.

fat = int(input("Digite o número fatorial: "))
total = 1
aux = fat
total2 = 1
print("O fatorial de {} equivale a: ".format(fat), end="")
while fat != 0:
    total *= fat
    print("{} ".format(fat), end="")
    if fat != 1:
        print("X ", end="")
    else:
        print("= ", end="")
    fat -= 1
print("{}".format(total))

for i in range(1, aux):
    total2 *= aux
    aux -= 1
print(total2)