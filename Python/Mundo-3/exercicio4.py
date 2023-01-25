#Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma tupla, no final, mostre:
#A) Quantas vezes apareceu o valor 9;
#B) Em que posição foi digitado o primeiro valor 3;
#C) Quais foram os número pares.

num = (int(input("Digite o primeiro valor: ")),
        int(input("Digite o segundo valor: ")),
        int(input("Digite o terceiro valor: ")),
        int(input("Digite o ultimo valor: ")))

print(num)

print("Na tupla aparece o número 9 um total de {} vezes".format(num.count(9)))
print("Na Tupla o valor 3 está na posição {}".format(num.index(3)+1))

print("Os valores pares são: ",end="")
for c in num:
    if c % 2 == 0:
        print("{} -> ".format(c),end="")
print("FIM")