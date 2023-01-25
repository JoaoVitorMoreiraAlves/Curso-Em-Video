#Crie um programa onde o usuário possa digitar sete valores número e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em valores crescentes.

numeros = [[],[]]

for i in range(0,7):
    num = int(input("Digite o {}º valor: ".format(i+1)))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print("-="*30)
print(f"Valores Pares: {numeros[0]}\nValores Impares: {numeros[1]}")