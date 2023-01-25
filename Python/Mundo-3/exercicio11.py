#Crie um programa que vai ler vários número e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitado, respectivamente.

#Ao final, mostre o conteúdo das três listas geradas.

num = []
impar = []
par = []
opinador = ""
while True:
    num.append(int(input("Digite o valor: ")))

    while opinador != "S" and opinador != "N":
        opinador = str(input("Deseja Continuar? [S/N]: ")).upper()[0]
    
    if opinador == "N":
        break
    else:
        opinador = ""

for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print("-=*"*15)
print(f"Lista normal: {num}")
print(f"Lista Impar: {impar}")
print(f"Lista Par: {par}")