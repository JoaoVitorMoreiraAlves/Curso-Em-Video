#Desenvolva um programa que leia seis número inteiro e mostre a soma apenas daqueles que foram pares, se o valor digitado for impar, desconsidere-os.
soma = 0
for i in range(1,7):
    num = int(input("Digite o valor: "))
    if (num%2 == 0):
        soma += num
print("A somatória dos valores pares é {}".format(soma))