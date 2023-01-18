#Faça um programa que leia três número e veja qual é o maior e qual é o menor.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 > n2 and n1 > n3:
    print("O número {} é o maior".format(n1))
    if n2 > n3:
        print("O número {} é o menor".format(n3))
    else:
        print("O número {} é o menor".format(n2))
if n2 > n1 and n2 > n3:
    print("O número {} é o maior".format(n2))
    if n1 > n3:
        print("O número {} é o menor".format(n3))
    else:
        print("O número {} é o menor".format(n1))
if n3 > n1 and n3 > n2:
    print("O número {} é o maior".format(n3))
    if n1 > n2:
        print("O número {} é o menor".format(n2))
    else:
        print("O número {} é o menor".format(n1))
if n1 == n2 and n2 == n3:
    print("Os três valores são iguais!!")